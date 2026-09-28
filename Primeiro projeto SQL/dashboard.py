import streamlit as st
import sqlite3
import pandas as pd


st.title("O Meu Primeiro Painel de Vendas em Python")
st.write("Bem-vindo ao sistema de análise de dados. Este painel foi construído 100% em Python!")


conexao = sqlite3.connect('banco_join.db')
query = '''
    SELECT Clientes.nome, Clientes.estado, Vendas.produto, Vendas.valor
    FROM Vendas
    JOIN Clientes ON Vendas.id_cliente = Clientes.id_cliente
'''
df = pd.read_sql_query(query, conexao)
conexao.close()


st.subheader("Tabela de Registos (Base de Dados)")
st.dataframe(df)


st.subheader("Faturação por Cliente")

faturacao_cliente = df.groupby('nome')['valor'].sum()
st.bar_chart(faturacao_cliente)
