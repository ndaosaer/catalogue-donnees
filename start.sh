#!/bin/bash

echo "======================================"
echo " Catalogue de Données - Démarrage"
echo "======================================"
echo ""

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo " Python 3 n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

echo " Python détecté : $(python3 --version)"
echo ""

# Installer les dépendances
echo " Installation des dépendances..."
pip install -r requirements.txt --break-system-packages

echo ""
echo " Dépendances installées"
echo ""

# Lancer l'application
echo " Lancement de l'application..."
echo ""
echo "================================================"
echo "L'application sera accessible sur :"
echo " http://localhost:5000"
echo "================================================"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter l'application"
echo ""

python3 app.py
