import requests


api_key = "your api_key"
city = input("Enter city:")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response  = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print(f"\nWeather in {city}")
    print(f"Temperature : {temp}C")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")

else:
    print(f"HTTPS Error occurse ({response.status_code})")
    print(response.text)

