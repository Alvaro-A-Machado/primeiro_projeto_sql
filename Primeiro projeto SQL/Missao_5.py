import requests


url_api = "https://economia.awesomeapi.com.br/last/BTC-BRL"

print("A ligar à Nuvem (AwesomeAPI) para recolher dados...")
resposta = requests.get(url_api)


dados_brutos = resposta.json()


preco_real = float(dados_brutos['BTCBRL']['bid'])

print(f"Preço atual do Bitcoin: R$ {preco_real:,.2f}")
