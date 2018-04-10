import requests
import json, io
import time


with open('key.txt', 'r') as f:
    key=f.readline().strip()

with open('26cities.txt', 'r') as f:
    cities = f.read().split('\n')

print(len(cities))

prices = []
for cityState in cities:
    city = cityState.split(',')[0]
    r = requests.get('https://www.numbeo.com/api/city_prices?api_key='+key+'&query='+city)
    if r.status_code != 200:
        print('error: ', city)
    prices.append(r.json())
    time.sleep(.2)

# r = requests.get("https://www.numbeo.com/api/cities?api_key="+key)
print(len(prices))

with open('cityPrices.json','w') as f:
    json.dump(prices, f, indent=4)
