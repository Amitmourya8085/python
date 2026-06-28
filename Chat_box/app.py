import requests
from flask import Flask,request,render_template,jsonify

API_KEY = "AQ.Ab8RN6IUSukRqfIf_gv2FuO3yaLuj6zT8XUnS36OOEN9c215Lg"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


