from bs4 import BeautifulSoup
import requests

weather_url = "https://www.ventusky.com/"

def show_weather(city_name: str):
    url = weather_url + city_name.lower()
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        time = soup.select("#forecast > div.forecast_block > table > thead > tr > th")[0].text.strip()
        temperature = soup.select("#forecast > div.forecast_block > table > tbody > tr > td > div")[0].text.strip()
        precipitation_thickness = soup.select("#forecast > div.forecast_block > table > tbody > tr > td > span")[0].text.strip()

        if len(soup.select("#forecast > div.forecast_block > table > tbody > tr > td > span")) > 1:
            precipitation_probability = soup.select("#forecast > div.forecast_block > table > tbody > tr > td > span > span")[0].text.strip()
        else:
            precipitation_probability = soup.select("#forecast > div.forecast_block > table > tbody > tr > td > span")[1].text.strip()

        wind_direction = soup.select("#forecast > div.forecast_block > table > tbody > tr > td > div")[1].text.strip()
        wind_speed = soup.select("#forecast > div.forecast_block > table > tbody > tr > td > div")[2].text.strip()

        print("Година:", time)
        print("Температура:", temperature)
        print("Товщина опадів:", precipitation_thickness)
        print("Імовірність опадів:", precipitation_probability)
        print("Напрям вітру:", wind_direction)
        print("Швидкість вітру:", wind_speed)
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")

show_weather("winnipeg")
