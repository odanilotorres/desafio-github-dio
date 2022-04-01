# Pacotes e requisicoes

import requests

response = requests.get('https://viacep.com.br/ws/18046525/json/')
# print(response.status_code)
print(response.text)
dados_cep = response.json()
print('Logradouro: ' + dados_cep['logradouro'])