from flask import Flask, render_template, request, jsonify
from lxml import etree
import os
import json
from datetime import datetime

app = Flask(__name__)

class DatasetParser:
    """Parse les fichiers XML DDI pour extraire les métadonnées"""
    
    def __init__(self, xml_path):
        self.xml_path = xml_path
        self.tree = etree.parse(xml_path)
        self.root = self.tree.getroot()
        # Namespace DDI
        self.ns = {'ddi': 'http://www.icpsr.umich.edu/DDI'}
    
    def get_text(self, xpath, default="Non spécifié"):
        """Récupère le texte d'un élément XML"""
        try:
            elements = self.root.xpath(xpath, namespaces=self.ns)
            if elements:
                text = elements[0].text
                return text.strip() if text else default
            return default
        except:
            return default
    
    def get_all_text(self, xpath):
        """Récupère tous les textes d'un xpath"""
        try:
            elements = self.root.xpath(xpath, namespaces=self.ns)
            return [elem.text.strip() for elem in elements if elem.text]
        except:
            return []
    
    def parse_metadata(self):
        """Parse toutes les métadonnées du dataset"""
        
        # Informations de base
        title = self.get_text('//ddi:stdyDscr/ddi:citation/ddi:titlStmt/ddi:titl')
        alt_title = self.get_text('//ddi:stdyDscr/ddi:citation/ddi:titlStmt/ddi:altTitl')
        id_number = self.get_text('//ddi:stdyDscr/ddi:citation/ddi:titlStmt/ddi:IDNo')
        
        # Résumé/Abstract
        abstract = self.get_text('//ddi:stdyDscr/ddi:stdyInfo/ddi:abstract')
        
        # Période de collecte
        start_date = self.get_text('//ddi:stdyDscr/ddi:stdyInfo/ddi:sumDscr/ddi:collDate[@event="start"]/@date')
        end_date = self.get_text('//ddi:stdyDscr/ddi:stdyInfo/ddi:sumDscr/ddi:collDate[@event="end"]/@date')
        
        # Pays et couverture
        nation = self.get_text('//ddi:stdyDscr/ddi:stdyInfo/ddi:sumDscr/ddi:nation')
        geog_cover = self.get_text('//ddi:stdyDscr/ddi:stdyInfo/ddi:sumDscr/ddi:geogCover')
        geog_unit = self.get_text('//ddi:stdyDscr/ddi:stdyInfo/ddi:sumDscr/ddi:geogUnit')
        
        # Univers et unité d'analyse
        universe = self.get_text('//ddi:stdyDscr/ddi:stdyInfo/ddi:sumDscr/ddi:universe')
        anly_unit = self.get_text('//ddi:stdyDscr/ddi:stdyInfo/ddi:sumDscr/ddi:anlyUnit')
        
        # Type de données
        data_kind = self.get_text('//ddi:stdyDscr/ddi:stdyInfo/ddi:sumDscr/ddi:dataKind')
        
        # Producteurs et auteurs
        producers = self.get_all_text('//ddi:stdyDscr/ddi:citation/ddi:prodStmt/ddi:producer')
        authors = self.get_all_text('//ddi:stdyDscr/ddi:citation/ddi:rspStmt/ddi:AuthEnty')
        
        # Financeurs
        funders = self.get_all_text('//ddi:stdyDscr/ddi:citation/ddi:prodStmt/ddi:fundAg')
        
        # Contact
        contact_email = self.get_text('//ddi:stdyDscr/ddi:citation/ddi:distStmt/ddi:contact/@email')
        contact_affiliation = self.get_text('//ddi:stdyDscr/ddi:citation/ddi:distStmt/ddi:contact/@affiliation')
        contact_uri = self.get_text('//ddi:stdyDscr/ddi:citation/ddi:distStmt/ddi:contact/@URI')
        
        # Méthodologie
        samp_proc = self.get_text('//ddi:stdyDscr/ddi:method/ddi:dataColl/ddi:sampProc')
        coll_mode = self.get_text('//ddi:stdyDscr/ddi:method/ddi:dataColl/ddi:collMode')
        
        # Taille de l'échantillon et variables
        case_qty = self.get_text('//ddi:fileDscr/ddi:fileTxt/ddi:dimensns/ddi:caseQnty', '0')
        var_qty = self.get_text('//ddi:fileDscr/ddi:fileTxt/ddi:dimensns/ddi:varQnty', '0')
        
        # Mots-clés
        keywords = self.get_all_text('//ddi:stdyDscr/ddi:stdyInfo/ddi:subject/ddi:keyword')
        
        # Copyright
        copyright_text = self.get_text('//ddi:stdyDscr/ddi:citation/ddi:prodStmt/ddi:copyright')
        
        # Conditions d'utilisation
        conditions = self.get_text('//ddi:stdyDscr/ddi:dataAccs/ddi:useStmt/ddi:conditions')
        
        # Ressources externes (fichiers de données)
        data_files = []
        try:
            file_elements = self.root.xpath('//ddi:fileDscr', namespaces=self.ns)
            for file_elem in file_elements:
                file_name = self.get_text('.//ddi:fileName', default='')
                file_uri = file_elem.get('URI', '')
                file_type = self.get_text('.//ddi:fileType', default='')
                if file_name or file_uri:
                    data_files.append({
                        'name': file_name,
                        'uri': file_uri,
                        'type': file_type
                    })
        except:
            pass
        
        return {
            'title': title,
            'alt_title': alt_title,
            'id': id_number,
            'abstract': abstract,
            'start_date': start_date,
            'end_date': end_date,
            'nation': nation,
            'geog_cover': geog_cover,
            'geog_unit': geog_unit,
            'universe': universe,
            'anly_unit': anly_unit,
            'data_kind': data_kind,
            'producers': producers,
            'authors': authors,
            'funders': funders,
            'contact_email': contact_email,
            'contact_affiliation': contact_affiliation,
            'contact_uri': contact_uri,
            'samp_proc': samp_proc,
            'coll_mode': coll_mode,
            'case_qty': case_qty,
            'var_qty': var_qty,
            'keywords': keywords,
            'copyright': copyright_text,
            'conditions': conditions,
            'data_files': data_files
        }

# Charger les datasets au démarrage
DATASETS = {}

def load_datasets():
    """Charge tous les fichiers XML du répertoire uploads"""
    # Chercher d'abord dans un dossier 'data' local, sinon dans le répertoire courant
    possible_dirs = [
        os.path.join(os.path.dirname(__file__), 'data'),  # Dossier data/ à côté de app.py
        os.path.join(os.path.dirname(__file__), 'uploads'),  # Dossier uploads/ à côté de app.py
        os.path.dirname(__file__)  # Répertoire courant (même dossier que app.py)
    ]
    
    xml_dir = None
    for dir_path in possible_dirs:
        if os.path.exists(dir_path):
            # Vérifier s'il y a des fichiers XML
            if any(f.endswith('.xml') for f in os.listdir(dir_path)):
                xml_dir = dir_path
                break
    
    if xml_dir is None:
        print("  Aucun fichier XML trouvé.")
        print(" Veuillez placer vos fichiers XML dans:")
        print(f"   - {os.path.join(os.path.dirname(__file__), 'data')}")
        print(f"   - OU directement dans: {os.path.dirname(__file__)}")
        return {}
    
    print(f" Chargement des datasets depuis: {xml_dir}")
    datasets = {}
    
    for filename in os.listdir(xml_dir):
        if filename.endswith('.xml'):
            filepath = os.path.join(xml_dir, filename)
            try:
                print(f"  Chargement de: {filename}")
                parser = DatasetParser(filepath)
                metadata = parser.parse_metadata()
                dataset_id = metadata['id']
                datasets[dataset_id] = {
                    'filename': filename,
                    'filepath': filepath,
                    'metadata': metadata
                }
                print(f"  {metadata['title']}")
            except Exception as e:
                print(f"  Erreur lors du chargement de {filename}: {e}")
    
    print(f"\n {len(datasets)} dataset(s) chargé(s) avec succès!\n")
    return datasets

# Charger les datasets
DATASETS = load_datasets()

def load_external_resources():
    """Charge les ressources externes depuis resources.json"""
    resources_file = os.path.join(os.path.dirname(__file__), 'resources.json')
    
    if not os.path.exists(resources_file):
        return {}
    
    try:
        with open(resources_file, 'r', encoding='utf-8') as f:
            resources = json.load(f)
            print(f" {len(resources)} groupe(s) de ressources externes chargé(s)")
            return resources
    except Exception as e:
        print(f" Erreur lors du chargement des ressources: {e}")
        return {}

# Charger les ressources externes
EXTERNAL_RESOURCES = load_external_resources()

@app.route('/')
def index():
    """Page d'accueil avec recherche"""
    return render_template('index.html', datasets=DATASETS)

@app.route('/about')
def about():
    """Page À propos"""
    return render_template('about.html', datasets=DATASETS)

@app.route('/catalog')
def catalog():
    """Liste complète des datasets"""
    return render_template('catalog.html', datasets=DATASETS, external_resources=EXTERNAL_RESOURCES)

@app.route('/dataset/<dataset_id>')
def dataset_detail(dataset_id):
    """Page détaillée d'un dataset"""
    if dataset_id not in DATASETS:
        return "Dataset non trouvé", 404
    
    dataset = DATASETS[dataset_id]
    # Récupérer les ressources pour ce dataset
    dataset_resources = EXTERNAL_RESOURCES.get(dataset_id, {})
    
    return render_template('dataset.html', dataset=dataset, external_resources=dataset_resources)

@app.route('/search')
def search():
    """Recherche dans les datasets"""
    query = request.args.get('q', '').lower()
    
    if not query:
        return jsonify({'results': []})
    
    results = []
    for dataset_id, dataset in DATASETS.items():
        metadata = dataset['metadata']
        # Recherche dans le titre, abstract et mots-clés
        searchable = f"{metadata['title']} {metadata['abstract']} {' '.join(metadata['keywords'])}".lower()
        
        if query in searchable:
            results.append({
                'id': dataset_id,
                'title': metadata['title'],
                'abstract': metadata['abstract'][:200] + '...' if len(metadata['abstract']) > 200 else metadata['abstract']
            })
    
    return jsonify({'results': results})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug, host='0.0.0.0', port=port)
