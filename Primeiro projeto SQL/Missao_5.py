import requests


url_api = "https://api.binance.com/api/v3/ticker/price?symbol=BTCBRL"

print("A ligar à Nuvem (Binance) para recolher dados...")
resposta = requests.get(url_api)


dados_brutos = resposta.json()


preco_real = float(dados_brutos['price'])


print(f"Preço atual do Bitcoin: R$ {preco_real:,.2f}")
