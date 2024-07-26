import pandas as pd
import streamlit as st
import sqlite3

#Conectando no SQLite3
conn= sqlite3.connect('../data/quotes.db')

#Importar os dados da tabela 'mercadolivre_items' em um DataFrame pandas

df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

#Encerrar a conexão com o banco de dados
conn.close()

#Nome da aplicação
st.title('Pesquisa de Mercado - Tênis esportivo masculino no Mercado Livre') 

#Aprimorar o layout com colunas para KPIs
st.subheader('KPIs principais do sistema')
col1, col2, col3 = st.columns(3) 

#Métrica 1 - Quantidade total de itens 
total_itens = df.shape[0]
col1.metric(label="Número total de itens", value=total_itens)

#Métrica 2 - Quantidade de marcas distintas
unique_brands = df['brand'].nunique()
col2.metric(label="Número de marcar únicas", value= unique_brands) 

#Métrica 3 - Valor médio dos itens novos (em reais)
average_new_price = df['new_price'].mean()
col3.metric(label="Preço médio novo (R$)", value= f"{average_new_price:.2f}") 

#Marcas mais frequentes até a página 10
st.subheader("Marcas mais encontradas até a 10ª página")
col1, col2 = st.columns([4, 2]) 
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False) 
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands) 

#Preço médio por marca
st.subheader("Preço médio por marca")
col1, col2 = st.columns([4, 2])
average_price_by_brand = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

#Nível de satisfação por marca 
st.subheader("Satisfação por marca")
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand) 