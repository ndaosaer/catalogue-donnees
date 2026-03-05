# 📊 Catalogue de Données - Application Flask

Catalogue web professionnel pour la diffusion et l'archivage de données statistiques, inspiré du système NADA.

## 🎯 Fonctionnalités

- ✅ **Page d'accueil** avec barre de recherche
- ✅ **Catalogue complet** avec liste des datasets
- ✅ **Pages détaillées** pour chaque enquête avec métadonnées complètes
- ✅ **Extraction automatique** des métadonnées depuis fichiers XML DDI
- ✅ **Recherche en temps réel** par titre, abstract et mots-clés
- ✅ **Design moderne** et responsive inspiré de NADA
- ✅ **Navigation par onglets** sur les pages de détail

## 📋 Prérequis

- Python 3.8+
- pip (gestionnaire de packages Python)

## 🚀 Installation

### 1. Installer les dépendances

```bash
pip install flask lxml
```

### 2. Structure des fichiers

```
Projet_Catalogue/
├── app.py                      # Application Flask principale
├── static/
│   └── css/
│       └── style.css          # Styles CSS
├── templates/
│   ├── base.html              # Template de base
│   ├── index.html             # Page d'accueil
│   ├── catalog.html           # Page catalogue
│   └── dataset.html           # Page détail dataset
└── uploads/                    # Vos fichiers XML DDI
    ├── Afrobarometer_2025_Benin.xml
    └── MICS_Benin_2021.xml
```

### 3. Placer vos fichiers XML

Copiez vos fichiers XML DDI dans un dossier (par défaut : `/mnt/user-data/uploads/`).

L'application charge automatiquement tous les fichiers `.xml` de ce répertoire.

### 4. Lancer l'application

```bash
python app.py
```

L'application sera accessible sur : **http://localhost:5000**

## 📂 Datasets actuellement chargés

### 1. Afrobarometer Round 10 - Bénin 2024
- **Type** : Enquête d'opinion publique
- **Échantillon** : 1 200 personnes
- **Variables** : 388
- **ID** : BEN-Afrobarometer-EOP-2025-001

### 2. MICS Bénin 2021-2022
- **Type** : Enquête par grappes à indicateurs multiples
- **Focus** : Enfants, femmes, ménages
- **ID** : DDI-BEN-INS-MICS-2014-V2.0

## 🎨 Personnalisation

### Modifier les couleurs

Éditez le fichier `static/css/style.css` et modifiez les variables CSS :

```css
:root {
    --primary-color: #2563eb;      /* Couleur principale */
    --secondary-color: #64748b;    /* Couleur secondaire */
    --dark-color: #1e293b;         /* Couleur sombre */
    /* ... */
}
```

### Ajouter votre logo

Dans `templates/base.html`, remplacez :

```html
<h1><a href="/">📊 Catalogue National de Données</a></h1>
```

par :

```html
<h1><a href="/"><img src="/static/img/logo.png" alt="Logo"></a></h1>
```

### Modifier les informations de contact

Éditez le footer dans `templates/base.html` :

```html
<div class="footer-section">
    <h3>Contact</h3>
    <p>Email: votre-email@domaine.com</p>
    <p>Tél: +229 XX XX XX XX</p>
</div>
```

## 🔧 Configuration avancée

### Changer le répertoire des fichiers XML

Dans `app.py`, modifiez :

```python
def load_datasets():
    xml_dir = '/votre/chemin/vers/xml'  # Modifier ici
    # ...
```

### Ajouter des formats de fichiers

L'application peut être étendue pour supporter d'autres formats (CSV, JSON, etc.) en modifiant la classe `DatasetParser`.

## 📱 Pages disponibles

- **/** : Page d'accueil avec recherche
- **/catalog** : Liste complète des datasets
- **/dataset/<id>** : Page détaillée d'un dataset
- **/search?q=<terme>** : API de recherche (JSON)

## 🎯 Utilisation

### Page d'accueil
- Vue d'ensemble avec statistiques
- Barre de recherche intelligente
- Cartes des enquêtes récentes

### Page Catalogue
- Liste complète des datasets
- Filtrage par recherche
- Métadonnées essentielles affichées

### Page Détail
- 4 onglets : Vue d'ensemble, Méthodologie, Production & Contact, Accès
- Métadonnées complètes extraites du XML
- Boutons d'action (impression, téléchargement)

## 📊 Métadonnées extraites

L'application extrait automatiquement :

- Titre et identifiant
- Résumé/Abstract
- Période de collecte
- Couverture géographique
- Producteurs et financeurs
- Méthodologie d'échantillonnage
- Mode de collecte
- Taille échantillon et nombre de variables
- Mots-clés
- Conditions d'utilisation
- Contacts

## 🚀 Déploiement en production

### Option 1 : Gunicorn (recommandé)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Option 2 : Docker

Créez un `Dockerfile` :

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install flask lxml gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Puis :

```bash
docker build -t catalogue-donnees .
docker run -p 5000:5000 catalogue-donnees
```

## 🛠️ Améliorations futures possibles

- [ ] Export des métadonnées en PDF
- [ ] Système d'authentification
- [ ] Téléchargement des microdonnées
- [ ] API REST complète
- [ ] Dashboard administrateur
- [ ] Support multilingue
- [ ] Intégration avec Google Analytics

## 📝 Notes techniques

- **Framework** : Flask 3.x
- **Parser XML** : lxml
- **Standard** : DDI (Data Documentation Initiative) 1.2.2
- **Frontend** : HTML5, CSS3, JavaScript (jQuery)
- **Responsive** : Design adaptatif pour mobile/tablette/desktop

## 🤝 Support

Pour toute question ou problème :
- Email : contact@catalogue-donnees.bj
- GitHub Issues : [Créer une issue]

## 📄 Licence

Projet académique - AS3 2025/2026
ENSAE Dakar - Archivage de données avec Nesstar Publisher

---

**Développé avec ❤️ pour faciliter l'accès aux données statistiques**
Voici le lien vers le catalogue: https://catalogue-donnees.onrender.com
