from flask import Flask, request, jsonify
from src.model import ask_ai

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")
    response = ask_ai(question)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)
