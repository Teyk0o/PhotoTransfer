# 🤝 Guide de Contribution

Merci de votre intérêt pour améliorer l'Organisateur de Photos ! Ce guide vous explique comment contribuer efficacement.

## 🚀 Démarrage Rapide

### 1. Fork et Clone
```bash
# Fork le repository sur GitHub, puis:
git clone https://github.com/VOTRE_USERNAME/PhotoTransfer.git
cd PhotoTransfer
```

### 2. Environment de Développement
```bash
# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt
pip install -e ".[dev]"  # Dépendances de développement
```

### 3. Tester l'Installation
```bash
python photo_organizer_v2.py
```

## 🐛 Signaler des Bugs

### Avant de Signaler
- Vérifiez les [issues existantes](../../issues)
- Testez avec la dernière version
- Reproduisez le bug de manière cohérente

### Template de Bug Report
```markdown
**Description du Bug**
Description claire et concise du problème.

**Étapes pour Reproduire**
1. Allez à '...'
2. Cliquez sur '....'
3. Faites défiler jusqu'à '....'
4. Observez l'erreur

**Comportement Attendu**
Ce qui devrait se passer.

**Captures d'Écran**
Si applicable, ajoutez des captures d'écran.

**Environment:**
 - OS: [ex: Windows 10]
 - Version Python: [ex: 3.11]
 - Version de l'app: [ex: 2.0.0]
```

## ✨ Proposer des Améliorations

### Template de Feature Request
```markdown
**Le Problème**
Description claire du problème que cette fonctionnalité résoudrait.

**La Solution**
Description claire de ce que vous aimeriez voir implémenté.

**Alternatives Considérées**
Autres solutions ou fonctionnalités que vous avez considérées.

**Contexte Supplémentaire**
Tout autre contexte ou captures d'écran sur la demande de fonctionnalité.
```

## 🔧 Développement

### Structure du Projet
```
PhotoTransfer/
├── photo_organizer_v2.py    # Application principale
├── build.py                 # Script de build
├── requirements.txt         # Dépendances
├── pyproject.toml          # Configuration projet
├── README.md               # Documentation
├── .github/workflows/      # GitHub Actions
└── tests/                  # Tests (à créer)
```

### Standards de Code

#### Style Python
- Utilisez [Black](https://black.readthedocs.io/) pour le formatage
- Respectez PEP 8
- Ajoutez des docstrings pour les fonctions importantes

```bash
# Formater le code
black photo_organizer_v2.py

# Vérifier le style
flake8 photo_organizer_v2.py
```

#### Conventions de Nommage
- **Variables/Fonctions**: `snake_case`
- **Classes**: `PascalCase`
- **Constantes**: `UPPER_CASE`
- **Fichiers**: `snake_case.py`

### Tests

#### Ajouter des Tests
```python
# tests/test_organizer.py
import unittest
from photo_organizer_v2 import PhotoOrganizer

class TestPhotoOrganizer(unittest.TestCase):
    def test_get_year_month_path(self):
        # Vos tests ici
        pass
```

#### Lancer les Tests
```bash
python -m pytest tests/
```

## 📝 Commits et Pull Requests

### Messages de Commit
Utilisez des messages clairs et descriptifs:

```bash
# Bon
git commit -m "✨ Ajouter support pour format HEIC"
git commit -m "🐛 Corriger duplication lors du tri"
git commit -m "📚 Mettre à jour documentation installation"

# Moins bon
git commit -m "fix"
git commit -m "update"
```

### Émojis de Commit (Optionnel)
- ✨ `:sparkles:` - Nouvelle fonctionnalité
- 🐛 `:bug:` - Correction de bug
- 📚 `:books:` - Documentation
- 🎨 `:art:` - Interface/Design
- ⚡ `:zap:` - Performance
- 🔧 `:wrench:` - Configuration
- 🚀 `:rocket:` - Deployment
- ✅ `:white_check_mark:` - Tests

### Pull Requests

#### Checklist avant PR
- [ ] Le code fonctionne localement
- [ ] Tests ajoutés si nécessaire
- [ ] Documentation mise à jour
- [ ] Code formaté avec Black
- [ ] Aucune régression introduite

#### Template de PR
```markdown
## 🎯 Objectif
Description claire de ce que fait cette PR.

## 🔄 Changements
- [ ] Nouvelle fonctionnalité X
- [ ] Correction du bug Y
- [ ] Amélioration de Z

## 🧪 Tests
- [ ] Tests automatisés ajoutés
- [ ] Testé manuellement sur Windows
- [ ] Testé avec différents types de photos

## 📸 Captures d'Écran
Si changements visuels, ajoutez des captures.

## ✅ Checklist
- [ ] Code testé localement
- [ ] Documentation mise à jour
- [ ] Changements décrits clairement
```

## 🔄 Workflow de Développement

### 1. Créer une Branche
```bash
git checkout -b feature/nom-de-la-fonctionnalite
# ou
git checkout -b fix/description-du-bug
```

### 2. Développer
- Faites vos modifications
- Testez régulièrement
- Committez fréquemment avec des messages clairs

### 3. Soumettre
```bash
git push origin feature/nom-de-la-fonctionnalite
```
Puis créez une Pull Request via l'interface GitHub.

## 🏗️ Build et Release

### Build Local
```bash
python build.py
```

### Créer une Release
Les releases sont automatiques via GitHub Actions lors de la création d'un tag:

```bash
git tag v2.1.0
git push origin v2.1.0
```

## 🆘 Aide et Support

### Où Obtenir de l'Aide
- 💬 [Discussions GitHub](../../discussions) - Questions générales
- 🐛 [Issues](../../issues) - Bugs et problèmes
- 📧 Email - Pour les questions sensibles

### Communauté
- Soyez respectueux et constructif
- Aidez les autres contributeurs
- Partagez vos idées et expériences

## 📄 Licence

En contribuant, vous acceptez que vos contributions soient sous licence MIT, identique au projet principal.

---

🙏 **Merci de contribuer à l'amélioration de l'Organisateur de Photos !**