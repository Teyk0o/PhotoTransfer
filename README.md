# 📸 Organisateur de Photos

Une application simple et moderne pour trier automatiquement vos photos par date. Pensée spécialement pour les utilisateurs non-techniques.

## ✨ Fonctionnalités

- 📁 **Tri automatique** par année et mois (ex: `2023/Août`, `2024/Janvier`)
- 🔍 **Détection intelligente** des dates via métadonnées EXIF ou date de fichier
- 🔄 **Anti-doublons** - Évite les copies inutiles lors de re-traitements
- 💾 **Sauvegarde des préférences** - Plus besoin de re-sélectionner les dossiers
- 📋 **Mode copie/déplacement** - Gardez vos originaux ou libérez de l'espace
- 🎨 **Interface moderne** avec émojis et textes d'aide
- ⚙️ **Option tri désactivable** - Regroupez simplement toutes vos photos

## 🚀 Installation

### Option 1: Exécutable Windows (Recommandé)
1. Téléchargez la dernière version depuis [Releases](../../releases)
2. Double-cliquez sur `Organisateur-Photos.exe`
3. C'est tout ! 🎉

### Option 2: Depuis le code source
```bash
# Cloner le projet
git clone https://github.com/VOTRE_USERNAME/PhotoTransfer.git
cd PhotoTransfer

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python photo_organizer_v2.py
```

## 📖 Guide d'utilisation

1. **📁 Sélectionnez votre dossier source** - Celui qui contient vos photos en désordre
2. **💾 Choisissez le dossier de destination** - Où vous voulez vos photos triées
3. **⚙️ Configurez les options** :
   - ✅ Tri par date : Crée des dossiers Année/Mois
   - ✅ Conserver originaux : Copie au lieu de déplacer
4. **🚀 Cliquez sur "ORGANISER MES PHOTOS"**
5. **🎉 Admirez le résultat !**

## 📂 Structure créée

```
📁 Dossier de destination/
├── 📁 2023/
│   ├── 📁 Janvier/
│   ├── 📁 Août/
│   └── 📁 Décembre/
└── 📁 2024/
    ├── 📁 Mars/
    └── 📁 Septembre/
```

## 🔧 Formats supportés

- **Photos courantes**: JPG, JPEG, PNG, TIFF, BMP, GIF, WEBP
- **Photos RAW**: CR2 (Canon), NEF (Nikon), ARW (Sony)
- **Formats modernes**: HEIC (iPhone)

## 🔄 Gestion des doublons

L'application détecte automatiquement les doublons en comparant:
1. **Taille du fichier** (vérification rapide)
2. **Contenu du fichier** (hash MD5)

**Résultat**: Les vrais doublons sont ignorés, les fichiers différents avec le même nom sont renommés (`photo_1.jpg`, `photo_2.jpg`, etc.)

## 🛠️ Développement

### Prérequis
- Python 3.8+
- Pillow (gestion d'images)
- piexif (métadonnées EXIF)

### Build local
```bash
# Installer PyInstaller
pip install pyinstaller

# Générer l'exécutable
python build.py
```

## 📝 Changelog

### v2.0.0
- ✨ Interface moderne avec émojis
- 💾 Sauvegarde automatique des préférences
- 🔄 Système anti-doublons intelligent
- 📁 Structure Année/Mois
- 🎯 Simplification pour utilisateurs non-techniques

### v1.0.0
- 🎉 Version initiale
- 📅 Tri par date basique
- 📋 Options copie/déplacement

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- 🐛 Signaler des bugs via les [Issues](../../issues)
- 💡 Proposer des améliorations
- 🔧 Soumettre des Pull Requests

## 📄 Licence

MIT License - Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- 🖼️ [Pillow](https://pillow.readthedocs.io/) - Traitement d'images Python
- 📷 [piexif](https://piexif.readthedocs.io/) - Gestion des métadonnées EXIF
- 🎨 Interface inspirée par les principes de design moderne

---

⭐ **Si cette application vous est utile, n'hésitez pas à laisser une étoile !**