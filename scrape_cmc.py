from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from config_cmc import API_KEY
import json

map_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"

parameters = {
  'symbol':'BTC,USDT,BNB'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(map_url, params=parameters)
    map_data = json.loads(response.text)
    for i in map_data['data']:
        print(i)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
