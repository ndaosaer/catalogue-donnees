"""
Script de test pour vérifier que le catalogue est correctement configuré
"""
import os
import sys

def test_installation():
    print("=" * 60)
    print(" Test de l'installation du Catalogue de Données")
    print("=" * 60)
    print()
    
    errors = []
    warnings = []
    
    # Test 1: Vérifier Python
    print("  Vérification de Python...")
    if sys.version_info >= (3, 8):
        print(f"    Python {sys.version_info.major}.{sys.version_info.minor} détecté")
    else:
        errors.append("Python 3.8+ requis")
        print(f"    Python {sys.version_info.major}.{sys.version_info.minor} (3.8+ requis)")
    print()
    
    # Test 2: Vérifier les modules
    print("  Vérification des modules Python...")
    modules = ['flask', 'lxml']
    for module in modules:
        try:
            __import__(module)
            print(f"    {module} installé")
        except ImportError:
            errors.append(f"Module {module} manquant")
            print(f"    {module} non installé - Exécutez: pip install {module}")
    print()
    
    # Test 3: Vérifier la structure des fichiers
    print("  Vérification de la structure des fichiers...")
    required_files = [
        'app.py',
        'requirements.txt',
        'templates/index.html',
        'templates/catalog.html',
        'templates/dataset.html',
        'templates/base.html',
        'static/css/style.css'
    ]
    
    for filepath in required_files:
        if os.path.exists(filepath):
            print(f"    {filepath}")
        else:
            errors.append(f"Fichier manquant: {filepath}")
            print(f"    {filepath} manquant")
    print()
    
    # Test 4: Chercher les fichiers XML
    print("  Recherche des fichiers XML...")
    xml_dirs = ['data', 'uploads', '.']
    xml_found = []
    
    for xml_dir in xml_dirs:
        if os.path.exists(xml_dir):
            files = [f for f in os.listdir(xml_dir) if f.endswith('.xml')]
            if files:
                print(f"    Dossier: {xml_dir}/")
                for f in files:
                    print(f"       {f}")
                    xml_found.extend(files)
    
    if not xml_found:
        warnings.append("Aucun fichier XML trouvé")
        print("     Aucun fichier XML trouvé!")
        print("    Placez vos fichiers XML dans:")
        print("      - data/ (recommandé)")
        print("      - ou directement dans le dossier courant")
    print()
    
    # Test 5: Tester le parser
    if xml_found and not errors:
        print("  Test du parser XML...")
        try:
            from app import DatasetParser
            # Trouver le premier fichier XML
            xml_file = None
            for xml_dir in xml_dirs:
                if os.path.exists(xml_dir):
                    files = [f for f in os.listdir(xml_dir) if f.endswith('.xml')]
                    if files:
                        xml_file = os.path.join(xml_dir, files[0])
                        break
            
            if xml_file:
                parser = DatasetParser(xml_file)
                metadata = parser.parse_metadata()
                print(f"    Parser fonctionne correctement")
                print(f"    Dataset détecté: {metadata['title'][:50]}...")
            else:
                warnings.append("Impossible de tester le parser (pas de XML)")
        except Exception as e:
            errors.append(f"Erreur du parser: {str(e)}")
            print(f"    Erreur: {str(e)}")
        print()
    
    # Résumé
    print("=" * 60)
    print(" RÉSUMÉ")
    print("=" * 60)
    
    if errors:
        print(f"\n {len(errors)} erreur(s) détectée(s):")
        for error in errors:
            print(f"   • {error}")
        print("\n  Corrigez ces erreurs avant de lancer l'application")
    
    if warnings:
        print(f"\n  {len(warnings)} avertissement(s):")
        for warning in warnings:
            print(f"   • {warning}")
    
    if not errors and not warnings:
        print("\n Tout est prêt !")
        print("\n Vous pouvez lancer l'application avec:")
        print("   python app.py")
        print("\n Puis ouvrez: http://localhost:5001")
    elif not errors:
        print("\n  Installation OK mais attention aux avertissements")
        print("\n Vous pouvez quand même lancer avec:")
        print("   python app.py")
    
    print("\n" + "=" * 60)
    return len(errors) == 0

if __name__ == "__main__":
    success = test_installation()
    sys.exit(0 if success else 1)
