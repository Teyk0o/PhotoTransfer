# 🚀 Deployment Guide

Guide for deploying and creating releases of Photo Organizer.

## 📋 Prerequisites

- Write access to the GitHub repository
- Python 3.8+ installed locally
- Git configured with your credentials

## 🔄 Release Workflow

### 1. Release Preparation

#### a) Version Update
Update the version in `pyproject.toml`:
```toml
[project]
version = "2.1.0"  # ← Update here
```

#### b) Complete Local Testing
```bash
# Install dependencies
pip install -r requirements.txt

# Test the application
python photo_organizer_v2.py

# Test local build
python build.py
```

#### c) Changelog Update
Update `README.md` changelog section:
```markdown
### v2.1.0
- ✨ New feature X
- 🐛 Fix bug Y
- 🎨 UI improvement Z
```

### 2. Release Creation

#### a) Commit and Push Changes
```bash
git add .
git commit -m "chore: prepare release v2.1.0"
git push origin main
```

#### b) Create and Push Tag
```bash
# Create tag locally
git tag -a v2.1.0 -m "Release version 2.1.0"

# Push tag (triggers GitHub Actions)
git push origin v2.1.0
```

#### c) GitHub Actions Runs Automatically
1. ✅ Build Windows executable
2. ✅ Generate changelog
3. ✅ Create GitHub release
4. ✅ Upload executable as asset

### 3. Release Verification

#### Verify everything works:
1. 🔗 [Go to GitHub Releases](../../releases)
2. ✅ Verify release is created
3. 📦 Download and test executable
4. 📝 Verify automatic changelog

## 🛠️ Local Build (Optional)

### Automatic Build Script
```bash
python build.py
```

### Manual Build with PyInstaller
```bash
# Installation
pip install pyinstaller

# Basic build
pyinstaller --onefile --windowed photo_organizer_v2.py

# Optimized build
pyinstaller \
  --onefile \
  --windowed \
  --name="Photo-Organizer" \
  --clean \
  --optimize=2 \
  photo_organizer_v2.py
```

## 📊 GitHub Actions (Details)

### Workflow Trigger
```yaml
on:
  push:
    tags:
      - 'v*'  # v1.0.0, v2.1.0, etc.
```

### Executed Jobs
1. **build-windows**: Compiles Windows executable
2. **create-release**: Creates GitHub release with assets
3. **notify-failure**: Notifies on failure (optional)

### Required Secrets
- `GITHUB_TOKEN` (automatic, no configuration needed)

## 🔧 GitHub Actions Configuration

### Environment Variables
```yaml
env:
  APP_NAME: "PhotoTransfer"  # Executable name
```

### Customization
To modify the workflow, edit `.github/workflows/release.yml`:

```yaml
# Change Python version
python-version: '3.11'

# Add platforms
strategy:
  matrix:
    os: [windows-latest, ubuntu-latest, macos-latest]
```

## 🐛 Troubleshooting

### Build Fails
```bash
# Check dependencies locally
pip install -r requirements.txt
python -c "import tkinter; import PIL; import piexif"

# Test local build
python build.py
```

### GitHub Actions Fails
1. 📋 Check logs in "Actions" tab
2. 🔍 Look at the failed section
3. 🛠️ Fix and re-push a new tag

### Tag Already Exists
```bash
# Delete local tag
git tag -d v2.1.0

# Delete remote tag
git push origin --delete v2.1.0

# Recreate with fixes
git tag -a v2.1.0 -m "Release version 2.1.0"
git push origin v2.1.0
```

## 📝 Versioning Conventions

### Semantic Versioning (SemVer)
- `v2.0.0` - Major version (breaking changes)
- `v2.1.0` - Minor version (new features)
- `v2.1.1` - Patch (bug fixes)

### Tag Types
- `v2.1.0` - Stable release
- `v2.1.0-beta.1` - Pre-release/beta
- `v2.1.0-alpha.1` - Alpha version

## 🎯 Release Checklist

### Before Release
- [ ] ✅ Local tests pass
- [ ] 📝 Version updated in `pyproject.toml`
- [ ] 📚 Documentation up to date
- [ ] 🔄 Changelog updated
- [ ] 🧪 Local build tested

### After Release
- [ ] ✅ GitHub release created
- [ ] 📦 Executable downloadable
- [ ] 🎯 Executable tested on clean machine
- [ ] 📢 Announcement (if necessary)

## 🚨 Rollback

### Delete Defective Release
1. 🗑️ Delete release on GitHub
2. 🏷️ Delete tag:
```bash
git push origin --delete v2.1.0
git tag -d v2.1.0
```
3. 🔧 Fix issues
4. 🚀 Recreate release with same tag

---

🎉 **Your application is now ready for automated deployment!**