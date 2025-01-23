import streamlit as st
import pandas as pd
import plotly.express as px

#Container 1º, introdução da comparação
with st.container():
    st.title('Comparação Rotten e IMDB')
    st.write('Essa análise faz a comparação dos dados dos programas pela nota do Rotten e do IMDB.')
    st.write('Nessa análise e possivel filtrar os dados por ano, gênero e plataforma que está disponivel, a comparação e feita através de um gráfico de barra onde logo acima do gráfico mostra a média de todas do "Rotten" e do "IMDB" é ja no gráfico podemos ver uma comparação em coluna.')

df = pd.read_csv('HBO-MAX-Content.csv', encoding='ISO-8859-1', sep=';')

#Container 2º, filtragem dos dados e visualização do gráfico
with st.container():
    df = pd.read_csv('HBO-MAX-Content.csv', encoding='ISO-8859-1', sep=';')

    # Filtros
    ano_selecionado = st.slider('Selecione o Ano:', min_value=df['year'].min(), max_value=df['year'].max())
    genero_selecionado = st.multiselect('Selecione o Gênero:', df.columns[9:37])

    # Obtendo as plataformas disponíveis
    plataformas_disponiveis = df.columns[37:]
    plataforma_selecionada = st.multiselect('Selecione a Plataforma:', plataformas_disponiveis)

    # Aplicando filtros
    filtro_ano = df['year'] == ano_selecionado

    # Filtrar por gênero
    if genero_selecionado:
        filtro_genero = df[genero_selecionado].eq(1).any(axis=1)
    else:
        filtro_genero = True

    # Filtrar por plataforma
    if plataforma_selecionada:
        filtro_plataforma = df[plataforma_selecionada].sum(axis=1)
    else:
        filtro_plataforma = True

    df_filtrado = df[filtro_ano & filtro_genero & filtro_plataforma]

    # Calculando métricas
    media_rotten = df_filtrado['rotten_score'].mean()
    media_imdb = df_filtrado['imdb_score'].mean()

    # Exibindo médias
    st.write(f'Média Rotten Tomatoes Score: {media_rotten:.2f}')
    st.write(f'Média IMDb Score: {media_imdb:.2f}')

    # Gráfico de barras interativo com Plotly Express
    fig = px.bar(df_filtrado, x='title', y=['rotten_score', 'imdb_score'],
                 title=f'Métricas por Filme ({ano_selecionado}, {genero_selecionado}, {plataforma_selecionada})',
                 labels={'value': 'Score'})
    st.plotly_chart(fig, use_container_width=True)
