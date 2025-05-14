import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_current_weather():
    # print(f"\n ***enter the city name:\n**")
    # city = input(f"\n ***enter the city name:\n**")
    # request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&unit=metric'
    #
    # wether_api = requests.get(request_url).json()
    # pprint(wether_api)

    print(f"\n *** get Current whether condition ***\n")

    city = input("Enter city name: \n")
    print("")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&unit=imperial'
    # print(request_url)

    weather_response = requests.get(request_url).json()
    pprint(weather_response)
    print(f'\n current wether for  {weather_response["name"]}')
    print(f'\n temp wether for  {weather_response["main"]["temp"]}')
    #u can access in the list
    print(f'\n Feelslike wether for  {weather_response["main"]["feels_like"]} and \n{weather_response["weather"][0]["description"]}')


if __name__ == "__main__":
    get_current_weather()
