import requests
from flask import Flask,request,render_template,jsonify

API_KEY = "AQ.Ab8RN6IyeWQsXf0KnPHoK9yyrcNAT4IgAX9l7FXyT1m5GclGtw"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask',methods=['POST'])
def ask_AM8085():
     user_prompt = request.json.get('prompt')
     payload = {
        "contents": [{
            "parts": [{"text": user_prompt}]
        }]
     } 
     
     header = {"Contents-Type":"applicatin/type"}

     response = requests.post(url=URL,json=payload,headers=header)
     data = response.json()

     answer = data['candidates'][0]['content']['parts'][0]['text']

     return jsonify({"response": answer})


if __name__=='__main__':
     app.run(debug=True)



