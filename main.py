from flask import Flask, request, jsonify
import openai
import os  # Dodajemy obsługę zmiennych środowiskowych

app = Flask(__name__)

# Pobranie klucza API z zmiennych środowiskowych
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": data["message"]}]
    )
    return jsonify(response.choices[0].message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
