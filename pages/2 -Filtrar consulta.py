import streamlit as st
import pandas as pd

#Container 1º, introdução da consulta
with st.container():
    st.title('Consulta de programas')
    st.write('A consulta dos dados compativeis com a filtragem será mostrado abaixo em formato de planilha retornando todos os dados referentes aos programas das filtragens usadas.')
    st.write('Agora pode ser ter uma melhor análise da base de dados filtrando os dados de acordo com a necessidade, com os filtros de ano, gênero e plataforma.')

#Container 2º, campos de filtragem 
with st.container():
    df = pd.read_csv('HBO-MAX-Content.csv', encoding='ISO-8859-1', sep=';')

    # Filtros
    ano_selecionado = st.slider('Selecione o Ano:', min_value=df['year'].min(), max_value=df['year'].max())
    genero_selecionado = st.multiselect('Selecione o Gênero:', df.columns[9:37])
    plataforma_selecionada = st.multiselect('Selecione as Plataformas:', df.columns[37:])

    # Aplicando filtros
    df_filtrado = df[(df['year'] == ano_selecionado) &
                    (df[genero_selecionado].eq(1).any(axis=1) if genero_selecionado else True) &
                    (df[plataforma_selecionada].sum(axis=1) > 0 if plataforma_selecionada else True)]

    # Exibindo resultados
    if not df_filtrado.empty:
        st.subheader('Resultados da Consulta:')
        st.table(df_filtrado)
    else:
        st.warning('Nenhum filme encontrado com os filtros selecionados.')
