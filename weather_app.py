import requests
from dotenv import load_dotenv
import os

load_dotenv()

def weather_responder(city):
    print("************************************")
    url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"
    
    weather_data = requests.get(url).json()
    
    return weather_data

if __name__ == '__main__':
    
    city = input("Please enter your city : ")
    
    weather_data = weather_responder(city)