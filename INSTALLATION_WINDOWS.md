#  Installation sur Windows - Guide Rapide

##  Prérequis

- Python 3.8+ installé sur votre PC
- Vos fichiers XML DDI (Afrobarometer_2025_Benin.xml et MICS_Benin_2021.xml)

##  Installation en 4 étapes

### Étape 1 : Décompresser l'archive

Décompressez `Catalogue_Donnees_Flask.zip` dans un dossier de votre choix, par exemple :
```
C:\Users\VotreNom\Desktop\Catalogue_Donnees_Flask\
```

### Étape 2 : Placer vos fichiers XML

**Option A - Créer un dossier "data" (RECOMMANDÉ)**
1. Dans le dossier `Catalogue_Donnees_Flask`, créez un nouveau dossier nommé `data`
2. Copiez vos fichiers XML dans ce dossier `data`

Structure finale :
```
Catalogue_Donnees_Flask/
├── app.py
├── data/                           ← CRÉER CE DOSSIER
│   ├── Afrobarometer_2025_Benin.xml
│   └── MICS_Benin_2021.xml
├── templates/
├── static/
└── ...
```

**Option B - Placer directement dans le dossier principal**
Copiez vos fichiers XML directement dans `Catalogue_Donnees_Flask/` :
```
Catalogue_Donnees_Flask/
├── app.py
├── Afrobarometer_2025_Benin.xml    ← ICI
├── MICS_Benin_2021.xml             ← ICI
├── templates/
└── ...
```

### Étape 3 : Lancer l'application

**Méthode 1 : Double-cliquer sur start.bat**
- Double-cliquez sur `start.bat`
- Une fenêtre noire s'ouvrira et installera automatiquement les dépendances
- L'application démarrera automatiquement

**Méthode 2 : Ligne de commande**
1. Ouvrez l'invite de commande (cmd)
2. Naviguez vers le dossier :
   ```cmd
   cd C:\Users\VotreNom\Desktop\Catalogue_Donnees_Flask
   ```
3. Installez les dépendances :
   ```cmd
   pip install -r requirements.txt
   ```
4. Lancez l'application :
   ```cmd
   python app.py
   ```

### Étape 4 : Ouvrir dans le navigateur

Ouvrez votre navigateur (Chrome, Firefox, Edge...) et allez sur :
```
http://localhost:5001
```

Vous devriez voir votre catalogue avec vos 2 enquêtes ! 

##  Vérification du bon fonctionnement

Quand vous lancez `python app.py`, vous devriez voir :

```
 Chargement des datasets depuis: C:\...\Catalogue_Donnees_Flask\data
    Chargement de: Afrobarometer_2025_Benin.xml
    Afrobarometer Round 10 – Bénin 2024
    Chargement de: MICS_Benin_2021.xml
    Bénin - Enquête par Grappe à Indicateurs Multiples MICS 2021-2022

 2 dataset(s) chargé(s) avec succès!

 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5001
```

##  Problèmes fréquents

### "Python n'est pas reconnu..."
**Solution** : Installez Python depuis python.org et cochez "Add Python to PATH"

### "Aucun fichier XML trouvé"
**Solution** : Vérifiez que vos fichiers .xml sont bien dans le dossier `data/` ou dans le dossier principal

### "Module 'flask' not found"
**Solution** : Exécutez `pip install -r requirements.txt`

### "Port 5001 is already in use"
**Solution** : 
1. Ouvrez `app.py`
2. Allez à la dernière ligne
3. Changez `port=5001` en `port=5002` (ou autre port libre)

### Les datasets ne s'affichent pas
**Solution** : 
1. Vérifiez les messages dans la console lors du démarrage
2. Assurez-vous que vos fichiers XML sont au format DDI valide
3. Regardez s'il y a des messages d'erreur rouges

##  Personnalisation

### Changer le port
Modifiez la dernière ligne de `app.py` :
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Changez 5001 en 8080
```

### Changer le titre
Modifiez `templates/base.html` ligne 12 :
```html
<h1><a href="/"> Votre Nouveau Titre</a></h1>
```

### Changer les couleurs
Modifiez `static/css/style.css` lignes 9-18 (variables CSS)

##  Besoin d'aide ?

Si vous rencontrez des problèmes :
1. Vérifiez que Python est bien installé : `python --version`
2. Vérifiez que les fichiers XML sont bien placés
3. Regardez les messages d'erreur dans la console
4. Consultez le README.md complet

---

Bon catalogue ! 
