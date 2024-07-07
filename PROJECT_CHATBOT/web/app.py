from flask import Flask, request, jsonify, render_template, send_from_directory
import mysql.connector
from mysql.connector import Error
from difflib import SequenceMatcher
import string
import requests
import spacy

app = Flask(__name__)

# Charger le modèle spaCy pour le français
nlp = spacy.load("fr_core_news_sm")

# Charger les mots-clés extraits
with open('../data/esp_keywords.txt', 'r', encoding='utf-8') as file:
    esp_keywords = file.read().split(", ")

def normalize_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def contains_esp_keywords(text):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc]
    return any(keyword in tokens for keyword in esp_keywords)

def get_best_response(question, responses):
    question = normalize_text(question)
    best_match = None
    highest_similarity = 0.0
    
    for response in responses:
        response_text = response.get("text", "")
        normalized_response_text = normalize_text(response_text)
        similarity = SequenceMatcher(None, question, normalized_response_text).ratio()
        
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = response_text
    
    threshold = 0.6
    if best_match and highest_similarity > threshold:
        return best_match
    else:
        return "Je suis désolé, je n'ai pas la réponse à cette question."

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/chat')
def serve_chat():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')

    # Vérifier si la question contient des mots-clés liés à l'ESP
    if not contains_esp_keywords(question):
        return jsonify({"response": ["Je suis désolé, mais je réponds uniquement aux questions concernant l'ESP. Veuillez poser des questions exclusivement sur l'ESP."]})

    rasa_url = "http://localhost:5005/webhooks/rest/webhook"

    try:
        response = requests.post(rasa_url, json={"sender": "user", "message": question})
        if response.ok:
            responses = response.json()
            messages = [r["text"] for r in responses if "text" in r]
            
            if not messages:
                messages = ["Je suis désolé, je n'ai pas la réponse à cette question."]
            
            print(f"Question: {question}, Réponse: {messages}")
            return jsonify({"response": messages})
        else:
            print(f"Erreur: Réponse HTTP non OK, statut: {response.status_code}")
            return jsonify({"response": ["Désolé, une erreur est survenue."]})
    except Exception as e:
        print(f"Exception: {str(e)}")
        return jsonify({"response": [f"Erreur de communication avec le serveur Rasa: {str(e)}"]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
