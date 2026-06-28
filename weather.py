import requests
import tkinter as tk

api_key = "dfba527088c26160a04332e6f7ab004f"
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

# UI setup
root = tk.Tk()
root.title("Weather App")

root.geometry("300x300")

title = tk.Label(root, text="Weather App 🌦️", font=("Arial", 16))
title.pack(pady=10)

city_entry = tk.Entry(root, width=25)
city_entry.pack(pady=10)

search_btn = tk.Button(root, text="Get Weather", command=get_weather)
search_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()    
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

