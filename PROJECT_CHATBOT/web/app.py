from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

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
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"

    # Liste des réponses génériques de Rasa
    generic_responses = [
        "Désolé, je ne comprends pas.",
        "Pouvez-vous reformuler ?",
        "Je ne suis pas sûr de comprendre.",
        "Pouvez-vous poser une autre question ?"
    ]

    try:
        response = requests.post(rasa_url, json={"sender": "user", "message": question})
        if response.ok:
            responses = response.json()
            messages = []
            for r in responses:
                text = r.get("text", "").strip()
                if text and text not in generic_responses:
                    messages.append(text)
                else:
                    messages.append("désolé, je ne comprends pas votre question")
            return jsonify({"response": messages})
        else:
            return jsonify({"response": ["Désolé, une erreur est survenue."]})
    except Exception as e:
        return jsonify({"response": [f"Erreur de communication avec le serveur Rasa: {str(e)}"]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
