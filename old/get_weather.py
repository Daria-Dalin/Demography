import configparser
import requests

config = configparser.ConfigParser()  # объект для обращения к ini

config.read('settings.ini')

key = config['Weather']['key']

res = requests.get('http://api.openweathermap.org/data/2.5/find',
                   params={'q': 'Санкт-Петербург',
                           'type': 'like',
                           'units': 'metric',
                           'APPID': key})
data = res.json()

temp = data['list'][0]['main']

print(f"'Температура:', {temp['temp']} °C")
print('Ощущается как:', temp['feels_like'])
print('Давление:', temp['pressure'])
print('Влажность:', temp['humidity'])
