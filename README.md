# 📸 Photo Organizer

[![Release](https://img.shields.io/github/v/release/Teyk0o/PhotoTransfer?style=for-the-badge&logo=github)](https://github.com/Teyk0o/PhotoTransfer/releases)
[![Downloads](https://img.shields.io/github/downloads/Teyk0o/PhotoTransfer/total?style=for-the-badge&logo=github)](https://github.com/Teyk0o/PhotoTransfer/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows-blue?style=for-the-badge&logo=windows)](https://github.com/Teyk0o/PhotoTransfer/releases)

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=flat)](https://docs.python.org/3/library/tkinter.html)
[![Build Status](https://img.shields.io/github/actions/workflow/status/Teyk0o/PhotoTransfer/release.yml?style=flat&logo=github-actions)](https://github.com/Teyk0o/PhotoTransfer/actions)
[![Issues](https://img.shields.io/github/issues/Teyk0o/PhotoTransfer?style=flat&logo=github)](https://github.com/Teyk0o/PhotoTransfer/issues)

A simple and modern application to automatically sort your photos by date. Specially designed for non-technical users.

## ✨ Features

- 📁 **Automatic sorting** by year and month (e.g., `2023/August`, `2024/January`)
- 🔍 **Smart date detection** via EXIF metadata or file date
- 🔄 **Anti-duplicate system** - Avoids unnecessary copies during re-processing
- 💾 **Settings persistence** - No need to re-select folders
- 📋 **Copy/Move modes** - Keep your originals or free up space
- 🎨 **Modern interface** with emojis and helpful texts
- ⚙️ **Optional sorting** - Simply group all your photos if desired

## 🚀 Installation

### Option 1: Windows Executable (Recommended)
1. Download the latest version from [Releases](../../releases)
2. Double-click on `Organisateur-Photos.exe`
3. That's it! 🎉

### Option 2: From source code
```bash
# Clone the project
git clone https://github.com/Teyk0o/PhotoTransfer
cd PhotoTransfer

# Install dependencies
pip install -r requirements.txt

# Run the application
python photo_organizer.py
```

## 📖 User Guide

1. **📁 Select your source folder** - The one containing your unsorted photos
2. **💾 Choose the destination folder** - Where you want your sorted photos
3. **⚙️ Configure options**:
   - ✅ Sort by date: Creates Year/Month folders
   - ✅ Keep originals: Copy instead of move
4. **🚀 Click "ORGANIZE MY PHOTOS"**
5. **🎉 Admire the result!**

## 📂 Created Structure

```
📁 Destination folder/
├── 📁 2023/
│   ├── 📁 January/
│   ├── 📁 August/
│   └── 📁 December/
└── 📁 2024/
    ├── 📁 March/
    └── 📁 September/
```

## 🔧 Supported Formats

- **Common photos**: JPG, JPEG, PNG, TIFF, BMP, GIF, WEBP
- **RAW photos**: CR2 (Canon), NEF (Nikon), ARW (Sony)
- **Modern formats**: HEIC (iPhone)

## 🔄 Duplicate Management

The application automatically detects duplicates by comparing:
1. **File size** (quick check)
2. **File content** (MD5 hash)

**Result**: True duplicates are ignored, different files with the same name are renamed (`photo_1.jpg`, `photo_2.jpg`, etc.)

## 🛠️ Development

### Prerequisites
- Python 3.8+
- Pillow (image handling)
- piexif (EXIF metadata)

### Local Build
```bash
# Install PyInstaller
pip install pyinstaller

# Generate executable
python build.py
```

### Contributing
We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

## 📝 Changelog

### v2.0.0
- ✨ Modern interface with emojis
- 💾 Automatic settings persistence
- 🔄 Smart anti-duplicate system
- 📁 Year/Month structure
- 🎯 Simplified for non-technical users

### v1.0.0
- 🎉 Initial version
- 📅 Basic date sorting
- 📋 Copy/move options

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs via [Issues](../../issues)
- 💡 Propose improvements
- 🔧 Submit Pull Requests

Please read our [Contributing Guidelines](CONTRIBUTING.md) first.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🖼️ [Pillow](https://pillow.readthedocs.io/) - Python image processing
- 📷 [piexif](https://piexif.readthedocs.io/) - EXIF metadata handling
- 🎨 Interface inspired by modern design principles

## 🌟 Support

If you find this application useful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting issues
- 💬 Sharing with friends
- 🤝 Contributing to the project

---

**⭐ If this application is useful to you, don't hesitate to leave a star!**