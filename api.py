import requests

url = "https://api.github.com/users/octocat"

response = requests.get(url)

# print(response.status_code)
# print(response.text)

data = response.json()
print(data["login"])
