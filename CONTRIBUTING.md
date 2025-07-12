# 🤝 Contributing Guide

Thank you for your interest in improving Photo Organizer! This guide explains how to contribute effectively.

## 🚀 Quick Start

### 1. Fork and Clone
```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/PhotoTransfer.git
cd PhotoTransfer
```

### 2. Development Environment
```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
pip install -e ".[dev]"  # Development dependencies
```

### 3. Test Installation
```bash
python photo_organizer_v2.py
```

## 🐛 Reporting Bugs

### Before Reporting
- Check [existing issues](../../issues)
- Test with the latest version
- Reproduce the bug consistently

### Bug Report Template
```markdown
**Bug Description**
Clear and concise description of the problem.

**Steps to Reproduce**
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected Behavior**
What should happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
 - OS: [e.g. Windows 10]
 - Python Version: [e.g. 3.11]
 - App Version: [e.g. 2.0.0]
```

## ✨ Proposing Enhancements

### Feature Request Template
```markdown
**The Problem**
Clear description of the problem this feature would solve.

**The Solution**
Clear description of what you'd like to see implemented.

**Alternatives Considered**
Other solutions or features you've considered.

**Additional Context**
Any other context or screenshots about the feature request.
```

## 🔧 Development

### Project Structure
```
PhotoTransfer/
├── photo_organizer_v2.py    # Main application
├── build.py                 # Build script
├── requirements.txt         # Dependencies
├── pyproject.toml          # Project configuration
├── README.md               # Documentation
├── .github/workflows/      # GitHub Actions
└── tests/                  # Tests (to be created)
```

### Code Standards

#### Python Style
- Use [Black](https://black.readthedocs.io/) for formatting
- Follow PEP 8
- Add docstrings for important functions

```bash
# Format code
black photo_organizer_v2.py

# Check style
flake8 photo_organizer_v2.py
```

#### Naming Conventions
- **Variables/Functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_CASE`
- **Files**: `snake_case.py`

### Tests

#### Adding Tests
```python
# tests/test_organizer.py
import unittest
from photo_organizer_v2 import PhotoOrganizer

class TestPhotoOrganizer(unittest.TestCase):
    def test_get_year_month_path(self):
        # Your tests here
        pass
```

#### Running Tests
```bash
python -m pytest tests/
```

## 📝 Commits and Pull Requests

### Branch Naming Conventions
Use conventional branch naming:

```bash
# Features
git checkout -b feat/add-heic-support
git checkout -b feat/user-authentication

# Bug fixes
git checkout -b fix/duplicate-sorting-issue
git checkout -b fix/memory-leak

# Documentation
git checkout -b docs/update-installation-guide

# Refactoring
git checkout -b refactor/optimize-file-processing

# Chores
git checkout -b chore/update-dependencies
```

### Commit Message Conventions
Follow [Conventional Commits](https://www.conventionalcommits.org/):

```bash
# Good examples
git commit -m "feat: add support for HEIC format"
git commit -m "fix: resolve duplicate files during sorting"
git commit -m "docs: update installation documentation"
git commit -m "refactor: optimize image processing performance"
git commit -m "test: add unit tests for file organizer"
git commit -m "chore: update dependencies to latest versions"

# With scope
git commit -m "feat(ui): add dark mode toggle"
git commit -m "fix(organizer): handle special characters in filenames"

# Breaking changes
git commit -m "feat!: change configuration file format"
git commit -m "feat(api)!: remove deprecated sorting methods"

# Bad examples
git commit -m "fix"
git commit -m "update"
git commit -m "working version"
```

### Commit Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements
- `ci`: CI/CD changes
- `build`: Build system changes

### Pull Requests

#### PR Title Convention
Use conventional commit format for PR titles:
```
feat: add HEIC image format support
fix: resolve duplicate file handling
docs: update contribution guidelines
```

#### Checklist before PR
- [ ] Code works locally
- [ ] Tests added if necessary
- [ ] Documentation updated
- [ ] Code formatted with Black
- [ ] No regressions introduced
- [ ] Branch follows naming convention
- [ ] Commits follow conventional format

#### PR Template
```markdown
## 🎯 Purpose
Clear description of what this PR does.

## 🔄 Changes
- [ ] New feature X
- [ ] Bug fix Y
- [ ] Improvement Z

## 🧪 Testing
- [ ] Automated tests added
- [ ] Manually tested on Windows
- [ ] Tested with different photo types

## 📸 Screenshots
If visual changes, add screenshots.

## ✅ Checklist
- [ ] Code tested locally
- [ ] Documentation updated
- [ ] Changes clearly described
- [ ] Follows branch naming convention
- [ ] Follows commit message convention
```

## 🔄 Development Workflow

### 1. Create a Branch
```bash
# Feature branch
git checkout -b feat/new-feature-name

# Bug fix branch
git checkout -b fix/bug-description

# Documentation branch
git checkout -b docs/documentation-update
```

### 2. Develop
- Make your changes
- Test regularly
- Commit frequently with clear conventional messages

### 3. Submit
```bash
git push origin feat/new-feature-name
```
Then create a Pull Request via GitHub interface.

## 🏗️ Build and Release

### Local Build
```bash
python build.py
```

### Creating a Release
Releases are automatic via GitHub Actions when creating a tag:

```bash
git tag v2.1.0
git push origin v2.1.0
```

## 🆘 Help and Support

### Where to Get Help
- 💬 [GitHub Discussions](../../discussions) - General questions
- 🐛 [Issues](../../issues) - Bugs and problems
- 📧 Email - For sensitive questions

### Community
- Be respectful and constructive
- Help other contributors
- Share your ideas and experiences

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License, same as the main project.

---

🙏 **Thank you for contributing to Photo Organizer!**