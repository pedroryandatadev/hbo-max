import streamlit as st
import pandas as pd
import plotly.express as px

#Container 1º, introdução da análise
with st.container():
    st.title('Média de score')
    st.write('Essa análise e da média score dos filmes de acordo com a nota do IMDB, porém nessa análise a especificações de filtragem que podem ser utilizadas.')
    st.write('A filtragem pode ser por ano de lançamento do filme ou série, também pode ser filtrada pelo gênero de classificação é pela plataforma que ele se encontra. Logo abaixo dos inputs de filtragem tem o valor de média da nota IMDB que é alterada de acordo com a consulta especificada.')

#Container 2º, Exibindo o gráficos com os filtros
with st.container():
    df = pd.read_csv('HBO-MAX-Content.csv', encoding='ISO-8859-1', sep=';')

    # Filtros
    ano_selecionado = st.slider('Selecione o Ano:', min_value=df['year'].min(), max_value=df['year'].max())
    genero_selecionado = st.multiselect('Selecione o Gênero:', df.columns[9:37])
    plataformas_selecionadas = st.multiselect('Selecione as Plataformas:', df.columns[37:])

    # Aplicando filtros
    df_filtrado = df[(df['year'] == ano_selecionado) &
                    (df[genero_selecionado].eq(1).any(axis=1) if genero_selecionado else True) &
                    (df[plataformas_selecionadas].sum(axis=1) > 0 if plataformas_selecionadas else True)]

    # Exibindo resultados
    if not df_filtrado.empty:
        media_pontuacao = df_filtrado['imdb_score'].mean()

        # Gráfico de barras interativo com Plotly Express
        fig = px.bar(df_filtrado, x='title', y='imdb_score', title=f'Média de Pontuação do IMDB por Programa: {media_pontuacao:.2f}',
                    labels={'imdb_score': 'Pontuação do IMDB', 'title': 'Título'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning('Nenhum programa encontrado com os filtros selecionados.')

