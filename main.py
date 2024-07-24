
import requests
from dotenv import load_dotenv
import os

# loading EVM
load_dotenv() 

# constants
URL = "http://api.weatherapi.com/v1/current.json"
TOKEN = os.getenv('TOKEN')


def weather(city, lang='en'):
  """
  This function fetches the information from the given city. Optional param is language.
  """
  # config
  params = {'key' : TOKEN,
           'q': city,
           'lang': lang}
  # network request
  res = requests.get(URL, params)

  # Converting to json
  data = res.json()

  # If location not found handle
  if 'error' in data:
    print("Location not Found!")
    return

  #Destructuring useful data
  forecast = {
    'state' : data['location']['region'],
    'temp_c' : data['current']['temp_c'],
    'temp_f' : data['current']['temp_f'],
    'condition' : data['current']['condition']['text']
  }    

  print(forecast)

user_location = input('Enter a location: ')
user_lang = input('Enter a lang code (en=English): ')

weather(user_location, user_lang)


# help(weather)
