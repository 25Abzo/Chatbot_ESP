import yaml
import spacy

# Charger le modèle spaCy pour le français
nlp = spacy.load("fr_core_news_sm")

# Charger le fichier nlu.yml
with open('data/nlu.yml', 'r', encoding='utf-8') as file:
    nlu_data = yaml.safe_load(file)

# Fonction pour extraire et normaliser les mots-clés
def extract_keywords(nlu_data):
    keywords = set()
    for intent in nlu_data['nlu']:
        for example in intent['examples'].split("\n"):
            doc = nlp(example.strip())
            for token in doc:
                if not token.is_stop and not token.is_punct and len(token.text) > 1:
                    keywords.add(token.lemma_.lower())
    return keywords

# Extraire les mots-clés
keywords = extract_keywords(nlu_data)

# Enregistrer les mots-clés dans un fichier
with open('data/esp_keywords.txt', 'w', encoding='utf-8') as file:
    file.write(", ".join(sorted(keywords)))

print(f"Mots-clés extraits : {sorted(keywords)}")
