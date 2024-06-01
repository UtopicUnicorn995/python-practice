import requests

API_KEY = '0502dfb4e8fa9ab4209619d3910412d6'
URL = 'https://api.openweathermap.org/data/2.5/weather?'
LAT = '10.772967863921224'
LON = '122.39125818306566'

request_url = requests.get(URL, lat=(LAT), lon=(LON), appid=(API_KEY))
print(request_url)