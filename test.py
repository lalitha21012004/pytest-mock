#A function depends on weather API to retrieve weather data.
#During testing,when we call external API,it occurs unexpected behavior.
#To avoid this,we can we use mock to simulate the behavior of API during testing without actually calling the API in mocktest.py file.

def fetch_weather_data(api_client):
    response = api_client.get("https://api.weather.com/data")
    if response.status_code == 200:
        return response.json()
    else:
        return None