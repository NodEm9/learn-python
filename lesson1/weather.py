import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather(city="Gelsenkirchen"): 
    API_KEY = os.getenv("API_KEY")
    # city = input('Enter the city name: ')
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={API_KEY}&q={city}&units=metric'
    response = requests.get(request_url)
    wealther_data = response.json()

    return wealther_data


if __name__ == '__main__':
    print('\n*** Current Weather ***\n ')

    city = input('\nEnter the city name: ')

    #  If the city is empty or with tab spaces, set it to default Gelsenkirchen
    if not bool(city.strip()):
        city = "Gelsenkirchen"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
    



