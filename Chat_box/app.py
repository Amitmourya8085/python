import requests
from flask import Flask, request, render_template, jsonify, session
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

app = Flask(__name__)

app.secret_key = os.getenv('secret_key') or 'fallback_secret_key'

@app.route('/')
def home():

    session['history'] = []
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_AM8085():
    user_prompt = request.json.get('prompt')
    if not user_prompt:
        return jsonify({'response": "Please enter something!'})
    
    chat_history = session.get('history', [])
    
    
    chat_history.append({
        "role": "user",
        "parts": [{"text": user_prompt}]
    })
     

    payload = {
        "contents": chat_history,
        "generationConfig": {
            "temperature": 0.2,       # Low temperature = focused and precise
            "maxOutputTokens": 150    # Short response constraint
        }
    } 
     
    header = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url=URL, json=payload, headers=header)
        data = response.json()

       
        answer = data['candidates'][0]['content']['parts'][0]['text']

    except Exception as e:
        print("Error:", e)
        answer = "Something went wrong. Please try again."

    chat_history.append({
        "role": "model",
        "parts": [{"text": answer}]
    })

    session['history'] = chat_history

    return jsonify({"response": answer})

@app.route('/clear', methods=['POST'])
def clear_chat():
    session['history'] = []
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)