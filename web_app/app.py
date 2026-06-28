import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# enter your api key use karne ke liye
API_KEY = "AQ.Ab8RN6IUSukRqfIf_gv2FuO3yaLuj6zT8XUnS36OOEN9c215Lg"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask_gemini():
    
    user_prompt = request.json.get('prompt') #index se input le ke json mai se dena
    
   
    payload = {
        "contents": [{
            "parts": [{"text": user_prompt}]
        }]
    }
    headers = {"Content-Type": "application/json"}

  
    response = requests.post(GEMINI_URL, json=payload, headers=headers)
    
   
    data = response.json()
    answer = data['candidates'][0]['content']['parts'][0]['text'] #take answer from respons-data-json
    
    
    return jsonify({"response": answer})

if __name__ == '__main__':
    app.run(debug=True)