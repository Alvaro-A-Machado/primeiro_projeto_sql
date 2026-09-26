import sqlite3
import pandas as pd

# 1. Cria a conexão com o banco de dados (ele cria o arquivo na hora!)
conexao = sqlite3.connect('meu_primeiro_banco.db')
cursor = conexao.cursor()

# 2. Comando SQL para criar uma tabela de "Vendas"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vendas (
        id INTEGER PRIMARY KEY,
        produto TEXT,
        valor REAL,
        quantidade INTEGER
    )
''')

# 3. Limpa a tabela (caso você rode o código mais de uma vez)
cursor.execute('DELETE FROM Vendas')

# 4. Comando SQL para inserir dados de mentirinha
dados_vendas = [
    (1, 'Notebook', 4500.00, 2),
    (2, 'Mouse', 150.00, 10),
    (3, 'Teclado', 250.00, 5),
    (4, 'Monitor', 1200.00, 3)
]
cursor.executemany('INSERT INTO Vendas VALUES (?, ?, ?, ?)', dados_vendas)
conexao.commit()  # Salva as alterações

# 5. O DESAFIO SQL: Buscar os produtos que renderam mais de R$ 1000 no total
query_sql = '''
    SELECT produto, valor, quantidade, (valor * quantidade) as faturamento_total
    FROM Vendas
    WHERE valor < 1000
    ORDER BY faturamento_total ASC
'''

# 6. Usando o Pandas (que você já sabe o básico) para ler o SQL e mostrar bonito
df_resultado = pd.read_sql_query(query_sql, conexao)

print("--- Resultado da Consulta SQL ---")
print(df_resultado)

# Fecha a conexão
conexao.close()
