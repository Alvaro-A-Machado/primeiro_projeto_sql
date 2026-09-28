import sqlite3
import pandas as pd

conexao = sqlite3.connect('meu_primeiro_banco.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vendas (
        id INTEGER PRIMARY KEY,
        produto TEXT,
        valor REAL,
        quantidade INTEGER
    )
''')

cursor.execute('DELETE FROM Vendas')

dados_vendas = [
    (1, 'Notebook', 4500.00, 2),
    (2, 'Mouse', 150.00, 10),
    (3, 'Teclado', 250.00, 5),
    (4, 'Monitor', 1200.00, 3)
]
cursor.executemany('INSERT INTO Vendas VALUES (?, ?, ?, ?)', dados_vendas)
conexao.commit()

query_sql = '''
    SELECT produto, valor, quantidade, (valor * quantidade) as faturamento_total
    FROM Vendas
    WHERE valor < 1000
    ORDER BY valor ASC
'''

df_resultado = pd.read_sql_query(query_sql, conexao)

print("--- Resultado da Consulta SQL ---")
print(df_resultado)


conexao.close()
