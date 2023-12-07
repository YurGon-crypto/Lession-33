import requests

def get_current_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        weather_data = response.json()
        return weather_data

    except requests.exceptions.RequestException as e:
        print(f"Помилка: {e}")
        return None


api_key = "cd84ca0665a96319700e1d7dff2e77de"
city_name = "Київ"
weather_data = get_current_weather(api_key, city_name)

if weather_data:
    print("Поточна погода:")
    print(f"Місто: {weather_data['name']}")
    print(f"Температура: {weather_data['main']['temp']} °C")
    print(f"Опис: {weather_data['weather'][0]['description']}")
