import requests
import sqlite3
from datetime import datetime

url_api = "https://blockchain.info/ticker"
resposta = requests.get(url_api)
dados = resposta.json()
preco_BRL = float(dados['BRL']['last'])
preco_USD = float(dados['USD']['last'])

data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conexao = sqlite3.connect('banco_join.db')
cursor = conexao.cursor()

# cursor.execute('DROP TABLE IF EXISTS Cotacoes_Bitcoin')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cotacoes_Bitcoin (
        data_hora TEXT,
        preco_BRL REAL,
        preco_USD REAL
    )
''')

cursor.execute(
    "INSERT INTO Cotacoes_Bitcoin (data_hora, preco_BRL, preco_USD) VALUES (?, ?, ?)", (data_hora, preco_BRL, preco_USD))
conexao.commit()
conexao.close()

print(
    f"Sucesso! Cotação de R$ {preco_BRL:,.2f}/U$ {preco_USD:,.2f} guardada no banco de dados em {data_hora}.")
