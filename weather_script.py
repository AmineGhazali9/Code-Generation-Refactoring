# Fetch weather data from OpenWeatherMap API
import os
import requests

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace this with your OpenWeatherMap API key

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()


def format_weather_data(data):
    main = data.get("main", {})
    weather_list = data.get("weather", [])
    weather_desc = weather_list[0]["description"] if weather_list else "Unknown"

    temperature = main.get("temp")
    humidity = main.get("humidity")
    feels_like = main.get("feels_like")

    return (
        f"Weather for {data.get('name', 'Unknown location')}:\n"
        f"  Condition: {weather_desc.capitalize()}\n"
        f"  Temperature: {temperature} °C\n"
        f"  Feels like: {feels_like} °C\n"
        f"  Humidity: {humidity}%\n"
    )


def main():
    city_name = input("Enter city name: ").strip()
    if API_KEY == "YOUR_OPENWEATHERMAP_API_KEY":
        print("Please set your OpenWeatherMap API key in the API_KEY variable at the top of this file.")
        return

    try:
        weather_data = fetch_weather(city_name)
        print(format_weather_data(weather_data))
    except requests.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except requests.RequestException as req_err:
        print(f"Request error: {req_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")


if __name__ == "__main__":
    main()
