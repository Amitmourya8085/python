import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# enter your api key use karne ke liye
API_KEY = "?"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

@app.route('/')
def home():
    return render_template('index.html')


