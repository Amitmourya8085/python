import requests

api_key = "yaha apna api key daalna"
url  = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

#gemini want exact json form
payload = {
    "contents": [{
        "parts": [{"text": "Explain the concept of an API to a 5-year-old in one sentence."}]
    }]
}

headers = {"Content-Type": "application/json"}

print("Sending request to Gemini... Please wait.")

response = requests.post(url,json=payload,headers=headers)

data = response.json()
answer = data['candidates'][0]['content']['parts'][0]['text']

print("\n Gemini answer-------------:")
print(answer)