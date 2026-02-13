#  Guide de Démarrage Rapide

## Installation en 3 étapes

### Étape 1 : Télécharger les fichiers
Téléchargez tous les fichiers du projet dans un dossier (ex: `Catalogue_Donnees`)

### Étape 2 : Installer les dépendances
Ouvrez un terminal/invite de commande dans le dossier et exécutez :

**Windows :**
```cmd
pip install -r requirements.txt
```

**Linux/Mac :**
```bash
pip install -r requirements.txt --break-system-packages
```

OU utilisez le script de démarrage :

**Linux/Mac :**
```bash
./start.sh
```

**Windows :**
```cmd
python app.py
```

### Étape 3 : Accéder à l'application
Ouvrez votre navigateur et allez sur :
```
http://localhost:5001
```

##  Ajouter vos propres données

1. Placez vos fichiers XML DDI dans le dossier `/mnt/user-data/uploads/` (ou modifiez le chemin dans `app.py`)
2. Redémarrez l'application
3. Vos datasets apparaîtront automatiquement !

##  Personnalisation rapide

### Changer le titre du site
Fichier : `templates/base.html` (ligne 12)
```html
<h1><a href="/"> VOTRE TITRE ICI</a></h1>
```

### Changer les couleurs
Fichier : `static/css/style.css` (lignes 9-18)
```css
:root {
    --primary-color: #2563eb;  /* Couleur principale */
}
```

### Modifier le pied de page
Fichier : `templates/base.html` (section footer)

##  Problèmes courants

### Port déjà utilisé
Si le port 5001 est occupé, modifiez dans `app.py` (dernière ligne) :
```python
app.run(debug=True, host='0.0.0.0', port=VOTRE_PORT)
```

### Modules non trouvés
Réinstallez les dépendances :
```bash
pip install flask lxml --upgrade
```

### Fichiers XML non détectés
Vérifiez que :
- Les fichiers sont bien des `.xml`
- Ils sont au format DDI valide
- Le chemin dans `app.py` est correct (ligne 115)

##  Besoin d'aide ?

Consultez le `README.md` complet pour plus de détails !

---

Bon archivage ! 
