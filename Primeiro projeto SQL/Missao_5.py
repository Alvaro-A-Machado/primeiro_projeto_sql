import requests

url_api = "https://blockchain.info/ticker"

print("A ligar à Nuvem (Blockchain.info) para recolher dados...")
resposta = requests.get(url_api)

dados_brutos = resposta.json()

preco_real = float(dados_brutos['BRL']['last'])

print(f"Preço atual do Bitcoin: R$ {preco_real:,.2f}")
