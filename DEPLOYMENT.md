# 🚀 Guide de Déploiement

Guide pour déployer et créer des releases de l'Organisateur de Photos.

## 📋 Prérequis

- Accès en écriture au repository GitHub
- Python 3.8+ installé localement
- Git configuré avec vos identifiants

## 🔄 Workflow de Release

### 1. Préparation de la Release

#### a) Mise à jour de la Version
Modifiez la version dans `pyproject.toml`:
```toml
[project]
version = "2.1.0"  # ← Mettre à jour ici
```

#### b) Test Local Complet
```bash
# Installer les dépendances
pip install -r requirements.txt

# Test de l'application
python photo_organizer_v2.py

# Test du build local
python build.py
```

#### c) Mise à jour du Changelog
Mettez à jour `README.md` section changelog:
```markdown
### v2.1.0
- ✨ Nouvelle fonctionnalité X
- 🐛 Correction du bug Y
- 🎨 Amélioration de l'interface Z
```

### 2. Création de la Release

#### a) Commit et Push des Changements
```bash
git add .
git commit -m "🚀 Préparer release v2.1.0"
git push origin main
```

#### b) Créer et Pousser le Tag
```bash
# Créer le tag localement
git tag -a v2.1.0 -m "Release version 2.1.0"

# Pousser le tag (déclenche GitHub Actions)
git push origin v2.1.0
```

#### c) GitHub Actions s'Exécute Automatiquement
1. ✅ Build Windows executable
2. ✅ Generate changelog
3. ✅ Create GitHub release
4. ✅ Upload executable as asset

### 3. Vérification de la Release

#### Vérifier que tout fonctionne:
1. 🔗 [Aller sur GitHub Releases](../../releases)
2. ✅ Vérifier que la release est créée
3. 📦 Télécharger et tester l'exécutable
4. 📝 Vérifier le changelog automatique

## 🛠️ Build Local (Optionnel)

### Script de Build Automatique
```bash
python build.py
```

### Build Manuel avec PyInstaller
```bash
# Installation
pip install pyinstaller

# Build basique
pyinstaller --onefile --windowed photo_organizer_v2.py

# Build optimisé
pyinstaller \
  --onefile \
  --windowed \
  --name="Organisateur-Photos" \
  --clean \
  --optimize=2 \
  photo_organizer_v2.py
```

## 📊 GitHub Actions (Détail)

### Workflow Trigger
```yaml
on:
  push:
    tags:
      - 'v*'  # v1.0.0, v2.1.0, etc.
```

### Jobs Exécutés
1. **build-windows**: Compile l'exécutable Windows
2. **create-release**: Crée la release GitHub avec assets
3. **notify-failure**: Notifie en cas d'échec (optionnel)

### Secrets Requis
- `GITHUB_TOKEN` (automatique, pas de configuration nécessaire)

## 🔧 Configuration GitHub Actions

### Variables d'Environment
```yaml
env:
  APP_NAME: "Organisateur-Photos"  # Nom de l'exécutable
```

### Customisation
Pour modifier le workflow, éditez `.github/workflows/release.yml`:

```yaml
# Changer la version Python
python-version: '3.11'

# Ajouter des plateformes
strategy:
  matrix:
    os: [windows-latest, ubuntu-latest, macos-latest]
```

## 🐛 Dépannage

### Build Échoue
```bash
# Vérifier les dépendances localement
pip install -r requirements.txt
python -c "import tkinter; import PIL; import piexif"

# Tester le build local
python build.py
```

### GitHub Actions Échoue
1. 📋 Vérifier les logs dans l'onglet "Actions"
2. 🔍 Regarder la section qui a échoué
3. 🛠️ Corriger et re-pousser un nouveau tag

### Tag Déjà Existant
```bash
# Supprimer tag local
git tag -d v2.1.0

# Supprimer tag distant
git push origin --delete v2.1.0

# Recréer avec corrections
git tag -a v2.1.0 -m "Release version 2.1.0"
git push origin v2.1.0
```

## 📝 Conventions de Versioning

### Semantic Versioning (SemVer)
- `v2.0.0` - Version majeure (changements incompatibles)
- `v2.1.0` - Version mineure (nouvelles fonctionnalités)
- `v2.1.1` - Patch (corrections de bugs)

### Types de Tags
- `v2.1.0` - Release stable
- `v2.1.0-beta.1` - Pre-release/beta
- `v2.1.0-alpha.1` - Version alpha

## 🎯 Checklist de Release

### Avant Release
- [ ] ✅ Tests locaux passent
- [ ] 📝 Version mise à jour dans `pyproject.toml`
- [ ] 📚 Documentation à jour
- [ ] 🔄 Changelog mis à jour
- [ ] 🧪 Build local testé

### Après Release
- [ ] ✅ Release GitHub créée
- [ ] 📦 Exécutable téléchargeable
- [ ] 🎯 Executable testé sur machine propre
- [ ] 📢 Annonce (si nécessaire)

## 🚨 Rollback (Retour en Arrière)

### Supprimer une Release Défectueuse
1. 🗑️ Supprimer la release sur GitHub
2. 🏷️ Supprimer le tag:
```bash
git push origin --delete v2.1.0
git tag -d v2.1.0
```
3. 🔧 Corriger les problèmes
4. 🚀 Recréer la release avec le même tag

---

🎉 **Votre application est maintenant prête pour un déploiement automatisé !**