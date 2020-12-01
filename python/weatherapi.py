import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=6ef32fb81c07b2e798f57554312ae35f' % zip)
##r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=cincinnati&appid=6ef32fb81c07b2e798f57554312ae35f')

data = r.json()

##print(type(data['weather'][0]['description']))
print(data['weather'][0]['description'])
