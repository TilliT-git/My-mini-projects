import requests

def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error retrieving data!")
        return None

    data = response.json()

    current = data["current_condition"][0]
    temp_c = current["temp_C"]
    feels_like = current["FeelsLikeC"]
    desc = current["weatherDesc"][0]["value"]

    print(f"Weather in the city {city}:")
    print(f"{temp_c}°C (feels like {feels_like}°C) — {desc}")

if __name__ == "__main__":
    city = input("Enter city: ")
    get_weather(city)

