#  Guide : Ajouter des Ressources Externes

## Vue d'ensemble

Les ressources externes vous permettent d'ajouter des liens vers :
-  **Fichiers de données** (CSV, SPSS, Stata, Excel)
-  **Questionnaires** et instruments de collecte (PDF)
-  **Rapports** et publications
-  **Documentation technique** et guides méthodologiques

##  Où sont-elles affichées ?

Les ressources apparaissent :
1. Dans la **page catalogue** (aperçu avec nombre de ressources)
2. Dans l'**onglet "Ressources externes"** de chaque dataset

##  Configuration

Les ressources sont configurées dans le fichier **`resources.json`** à la racine du projet.

### Structure du fichier

```json
{
  "ID-DU-DATASET": {
    "data_files": [...],
    "questionnaires": [...],
    "reports": [...],
    "documentation": [...]
  }
}
```

### Identifier l'ID du dataset

L'ID est visible dans :
- L'URL de la page détail : `/dataset/BEN-Afrobarometer-EOP-2025-001`
- Le fichier XML DDI : balise `<IDNo>`
- En bas de chaque carte du catalogue

##  Format d'une ressource

Chaque ressource suit ce format :

```json
{
  "name": "Nom de la ressource",
  "description": "Description détaillée du fichier",
  "type": "pdf",
  "icon": "📄",
  "url": "https://exemple.com/fichier.pdf",
  "size": "2.5 MB"
}
```

### Champs expliqués

| Champ | Description | Exemples |
|-------|-------------|----------|
| `name` | Nom affiché | "Questionnaire principal", "Données SPSS" |
| `description` | Description détaillée | "Fichier de microdonnées au format SPSS" |
| `type` | Type de fichier | "pdf", "spss", "stata", "csv", "xlsx" |
| `icon` | Emoji affiché | 📊 📝 📄 📑 📚 📖 📋 |
| `url` | Lien de téléchargement | URL complète vers le fichier |
| `size` | Taille du fichier | "2.5 MB", "850 KB" |

##  Exemples pratiques

### Exemple 1 : Ajouter un fichier de données

```json
{
  "name": "Données CSV complètes",
  "description": "Base de données complète au format CSV",
  "type": "csv",
  "icon": "📄",
  "url": "https://monsite.com/data/enquete.csv",
  "size": "5.2 MB"
}
```

### Exemple 2 : Ajouter un questionnaire

```json
{
  "name": "Questionnaire Femmes",
  "description": "Questionnaire individuel pour femmes de 15-49 ans",
  "type": "pdf",
  "icon": "📝",
  "url": "https://monsite.com/docs/questionnaire_femmes.pdf",
  "size": "1.8 MB"
}
```

### Exemple 3 : Ajouter un rapport

```json
{
  "name": "Rapport national 2024",
  "description": "Rapport complet des résultats de l'enquête",
  "type": "pdf",
  "icon": "📄",
  "url": "https://monsite.com/rapports/rapport_2024.pdf",
  "size": "12.5 MB"
}
```

##  Icônes recommandées

| Type de ressource | Icône suggérée |
|-------------------|----------------|
| Fichiers SPSS |  |
| Fichiers Stata |  |
| Fichiers CSV |  |
| Fichiers Excel |  |
| Questionnaires | 📝 |
| Manuels | 📖 |
| Rapports | 📄 |
| Documents techniques | 📑 |
| Codebooks | 📚 |
| Notes de synthèse | 📋 |
| Guides méthodologiques | ⚙️ |

## 📋 Template complet

Voici un template pour ajouter un nouveau dataset :

```json
{
  "VOTRE-ID-DATASET": {
    "data_files": [
      {
        "name": "Données SPSS",
        "description": "Fichier de microdonnées au format SPSS",
        "type": "spss",
        "icon": "📊",
        "url": "https://exemple.com/data.sav",
        "size": "3.5 MB"
      }
    ],
    "questionnaires": [
      {
        "name": "Questionnaire principal",
        "description": "Instrument de collecte principal",
        "type": "pdf",
        "icon": "📝",
        "url": "https://exemple.com/questionnaire.pdf",
        "size": "1.2 MB"
      }
    ],
    "reports": [
      {
        "name": "Rapport final",
        "description": "Rapport complet de l'enquête",
        "type": "pdf",
        "icon": "📄",
        "url": "https://exemple.com/rapport.pdf",
        "size": "8.5 MB"
      }
    ],
    "documentation": [
      {
        "name": "Guide méthodologique",
        "description": "Description de la méthodologie d'enquête",
        "type": "pdf",
        "icon": "📑",
        "url": "https://exemple.com/methodologie.pdf",
        "size": "2.3 MB"
      }
    ]
  }
}
```

## 🔄 Appliquer les modifications

1. Éditez le fichier `resources.json`
2. Sauvegardez vos modifications
3. Redémarrez l'application : `python app.py`
4. Actualisez votre navigateur

Les nouvelles ressources apparaîtront immédiatement !

##  Points d'attention

### URLs valides
- Utilisez des URLs complètes : `https://exemple.com/fichier.pdf`
- Vérifiez que les liens sont accessibles
- Privilégiez des liens permanents

### Taille des fichiers
- Indiquez la taille réelle du fichier
- Format : "X.X MB" ou "XXX KB"
- Aide l'utilisateur à estimer le temps de téléchargement

### Catégories
Vous pouvez omettre une catégorie si vous n'avez pas de ressources :

```json
{
  "MON-DATASET": {
    "data_files": [...],
    "questionnaires": [...]
    // Pas de "reports" ni "documentation" = OK
  }
}
```

##  Hébergement des fichiers

### Options d'hébergement

1. **Site web institutionnel**
   - Ex: `https://www.insae-bj.org/docs/rapport.pdf`
   
2. **Services cloud**
   - Google Drive (lien de partage direct)
   - Dropbox
   - OneDrive
   
3. **Plateformes spécialisées**
   - NADA Catalog
   - Microdata Library
   - HDX (Humanitarian Data Exchange)

### Obtenir un lien direct

**Google Drive :**
1. Partager le fichier → "Tous les utilisateurs ayant le lien"
2. URL format : `https://drive.google.com/file/d/ID/view`
3. Modifier en : `https://drive.google.com/uc?id=ID&export=download`

## 💡 Conseils

- **Organisez par type** : Séparez clairement données, docs et rapports
- **Descriptions claires** : Expliquez le contenu en 1-2 phrases
- **Mettez à jour** : Vérifiez régulièrement que les liens fonctionnent
- **Tailles précises** : Aidez l'utilisateur à planifier ses téléchargements

## 📞 Besoin d'aide ?

Consultez le fichier `resources.json` fourni pour voir des exemples complets avec Afrobarometer et MICS.

---

Bonne configuration ! 📚✨
