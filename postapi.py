import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "My First Post",
    "body": "Learning API in Python",
    "userId": 1
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())