#!/usr/bin/env python3
"""
Script de build pour créer l'exécutable Windows de l'Organisateur de Photos
"""

import os
import subprocess
import sys
from pathlib import Path

def build_executable():
    """Génère l'exécutable avec PyInstaller"""
    
    print("🔨 Génération de l'exécutable Organisateur de Photos...")
    
    # Vérifier que PyInstaller est installé
    try:
        import PyInstaller
        print(f"✅ PyInstaller {PyInstaller.__version__} détecté")
    except ImportError:
        print("❌ PyInstaller non trouvé. Installation...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Configuration PyInstaller
    main_script = "photo_organizer.py"
    app_name = "PhotoTransfer"
    
    # Options PyInstaller
    pyinstaller_args = [
        "pyinstaller",
        "--onefile",                    # Un seul fichier exécutable
        "--windowed",                   # Pas de console (GUI uniquement)
        f"--name={app_name}",          # Nom de l'exécutable
        "--clean",                      # Nettoyer le cache
        "--noconfirm",                 # Pas de confirmation
        
        # Métadonnées de l'exécutable
        "--add-data", "requirements.txt;.",  # Inclure requirements.txt
        
        # Optimisations
        "--optimize", "2",              # Optimisation bytecode
        "--strip",                      # Retirer les symboles debug
        
        # Icône (si disponible)
        # "--icon=icon.ico",
        
        main_script
    ]
    
    # Ajouter des données supplémentaires si nécessaire
    if os.path.exists("README.md"):
        pyinstaller_args.extend(["--add-data", "README.md;."])
    
    try:
        # Lancer PyInstaller
        print("🚀 Lancement de PyInstaller...")
        result = subprocess.run(pyinstaller_args, check=True, capture_output=True, text=True)
        
        print("✅ Build réussi !")
        print(f"📦 Exécutable généré: dist/{app_name}.exe")
        
        # Vérifier que le fichier existe
        exe_path = Path("dist") / f"{app_name}.exe"
        if exe_path.exists():
            size_mb = exe_path.stat().st_size / (1024 * 1024)
            print(f"📏 Taille: {size_mb:.1f} MB")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors du build:")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False

def clean_build_files():
    """Nettoie les fichiers temporaires de build"""
    import shutil
    
    print("🧹 Nettoyage des fichiers temporaires...")
    
    # Dossiers à supprimer
    dirs_to_clean = ["build", "__pycache__"]
    files_to_clean = ["*.spec"]
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"🗑️ Supprimé: {dir_name}/")
    
    # Supprimer les fichiers .spec
    for spec_file in Path(".").glob("*.spec"):
        spec_file.unlink()
        print(f"🗑️ Supprimé: {spec_file}")

def main():
    """Fonction principale"""
    print("📸 Organisateur de Photos - Script de Build")
    print("=" * 50)
    
    # Vérifier que le script principal existe
    if not os.path.exists("photo_organizer.py"):
        print("❌ Fichier photo_organizer.py non trouvé!")
        return 1
    
    # Installer les dépendances si nécessaire
    if os.path.exists("requirements.txt"):
        print("📦 Installation des dépendances...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Générer l'exécutable
    success = build_executable()
    
    if success:
        print("\n🎉 Build terminé avec succès !")
        print("💡 Conseil: Testez l'exécutable avant de le distribuer")
        
        # Nettoyer les fichiers temporaires
        clean_build_files()
        
        return 0
    else:
        print("\n❌ Échec du build")
        return 1

if __name__ == "__main__":
    sys.exit(main())