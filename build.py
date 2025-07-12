#!/usr/bin/env python3
"""
Build script to create the Windows executable for Photo Organizer
"""

import os
import subprocess
import sys
from pathlib import Path

def build_executable():
    """Generate executable with PyInstaller"""
    
    print("🔨 Building Photo Organizer executable...")
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print(f"✅ PyInstaller {PyInstaller.__version__} detected")
    except ImportError:
        print("❌ PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # PyInstaller configuration
    main_script = "photo_organizer.py"
    app_name = "PhotoTransfer"
    
    # PyInstaller options
    pyinstaller_args = [
        "pyinstaller",
        "--onefile",                    # Single executable file
        "--windowed",                   # No console (GUI only)
        f"--name={app_name}",          # Executable name
        "--clean",                      # Clean cache
        "--noconfirm",                 # No confirmation
        
        # Executable metadata
        "--add-data", "requirements.txt;.",  # Include requirements.txt
        
        # Optimizations
        "--optimize", "2",              # Bytecode optimization
        "--strip",                      # Remove debug symbols
        
        # Icon (if available)
        # "--icon=icon.ico",
        
        main_script
    ]
    
    # Add additional data if necessary
    if os.path.exists("README.md"):
        pyinstaller_args.extend(["--add-data", "README.md;."])
    
    try:
        # Launch PyInstaller
        print("🚀 Launching PyInstaller...")
        result = subprocess.run(pyinstaller_args, check=True, capture_output=True, text=True)
        
        print("✅ Build successful!")
        print(f"📦 Executable generated: dist/{app_name}.exe")
        
        # Check if file exists
        exe_path = Path("dist") / f"{app_name}.exe"
        if exe_path.exists():
            size_mb = exe_path.stat().st_size / (1024 * 1024)
            print(f"📏 Size: {size_mb:.1f} MB")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build error:")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False

def clean_build_files():
    """Clean temporary build files"""
    import shutil
    
    print("🧹 Cleaning temporary files...")
    
    # Folders to delete
    dirs_to_clean = ["build", "__pycache__"]
    files_to_clean = ["*.spec"]
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"🗑️ Deleted: {dir_name}/")
    
    # Delete .spec files
    for spec_file in Path(".").glob("*.spec"):
        spec_file.unlink()
        print(f"🗑️ Deleted: {spec_file}")

def main():
    """Main function"""
    print("📸 Photo Organizer - Build Script")
    print("=" * 50)
    
    # Check if main script exists
    if not os.path.exists("photo_organizer.py"):
        print("❌ File photo_organizer.py not found!")
        return 1
    
    # Install dependencies if necessary
    if os.path.exists("requirements.txt"):
        print("📦 Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Generate executable
    success = build_executable()
    
    if success:
        print("\n🎉 Build completed successfully!")
        print("💡 Tip: Test the executable before distributing")
        
        # Clean temporary files
        clean_build_files()
        
        return 0
    else:
        print("\n❌ Build failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())