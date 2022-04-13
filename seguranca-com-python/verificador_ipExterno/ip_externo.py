import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'
resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
city = dados['city']
country = dados['country']
region = dados['region']
print('Detalhes do IP externo: \n')
print(f'Ip: {ip} \nOrg: {org} \nCidade: {city} \nPais: {country} \nRegiao: {region}')
