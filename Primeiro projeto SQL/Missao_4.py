import sqlite3
import pandas as pd

conexao = sqlite3.connect('banco_join.db')
cursor = conexao.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        id_cliente INTEGER PRIMARY KEY,
        nome TEXT,
        estado TEXT
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vendas (
        id_venda INTEGER PRIMARY KEY,
        id_cliente INTEGER,
        produto TEXT,
        valor REAL
    )
''')


cursor.execute('DELETE FROM Clientes')
cursor.execute('DELETE FROM Vendas')

dados_clientes = [
    (1, 'Ana', 'MG'),
    (2, 'Carlos', 'SP'),
    (3, 'Beatriz', 'RJ')
]
dados_vendas = [
    (101, 1, 'Notebook', 4500.00),
    (102, 1, 'Mouse', 150.00),
    (103, 2, 'Monitor', 1200.00)
]

cursor.executemany('INSERT INTO Clientes VALUES (?, ?, ?)', dados_clientes)
cursor.executemany('INSERT INTO Vendas VALUES (?, ?, ?, ?)', dados_vendas)
conexao.commit()

print("Tabelas criadas e dados inseridos com sucesso!")

query_cruzamento = '''
    SELECT 
        Clientes.nome,
        Clientes.estado,
        Vendas.produto,
        Vendas.valor
    FROM Vendas
    JOIN Clientes ON Vendas.id_cliente = Clientes.id_cliente
'''

df_resultado = pd.read_sql_query(query_cruzamento, conexao)

print("\n--- Relatório Final com JOIN ---")
print(df_resultado)

conexao.close()
