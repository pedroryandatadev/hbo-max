import streamlit as st
import pandas as pd 

#Container 1º, mostrando o dataframe
with st.container():
    st.title('Informações da Base')
    st.write('O conjunto de dados HBO Content fornece informações abrangentes sobre os programas de TV e filmes disponíveis na HBO e HBO Max. Ele contém detalhes sobre vários aspectos do conteúdo, como título, tipo (seja um programa de TV ou filme), ano de lançamento, classificação (indicando a faixa etária apropriada), pontuação IMDb (uma medida de popularidade e qualidade), rotten_score (pontuação podre), década (a década em que o conteúdo foi lançado) e intervalo de pontuação da IMDb (categorizando a faixa de popularidade).')
    st.write('Além disso, inclui valores binários que indicam se o conteúdo pertence a gêneros específicos, como Ação/Aventura, Animação, Biografia, Infantil, Comédia, Crime, Culto, Documentário, Drama, Família, Fantasia, Comida, Game, Show, História, Terror, Independente, LGBTQ, Musical, Mistério, Realidade, Romance, Ficção Científica, Esporte, Stand-up/Talk, Thriller, Viagem. Esses indicadores de gênero permitem que os usuários filtrem o conteúdo com base em suas preferências.')

    st.subheader('Como foi conseguida a base?')
    st.write('A Base de Dados foi conseguida por meio do site "kaggle" que é uma plataforma de competição de ciência de dados e uma comunidade online de cientistas de dados e profissionais de aprendizado de máquina da Google LLC.')
    st.write('Link da base: https://www.kaggle.com/datasets/thedevastator/hbo-and-hbo-max-content-dataset')

#Container 2º, mostrando o dataframe
with st.container():
    st.title('Visualização do Dataframe')
    df = pd.read_csv('HBO-MAX-Content.csv', encoding='ISO-8859-1', sep=';')

    st.write(df)

#Container 3º, detalhando como funciona das colunas
with st.container():
    st.title('Detalhes das colunas')
    st.write('Informações de como funciona a base, especificação das colunas:')
    st.markdown('* **title:** Corresponde ao nome do filme ou série.')
    st.markdown('* **type:** Identifica o tipo do conteúdo se e do tipo filme (movie) ou série (TV).')
    st.markdown('* **year:** Ano de lançamento.')
    st.markdown('* **rating:** Avaliação do filme ou série.')
    st.markdown('* **year:** Ano de lançamento.')
    st.markdown('* **imdb_score:** Nota de avaliação do IMDB.')
    st.markdown('* **rotten_score:** Pontuação podre, mostra a potuação negativa do filme ou série.')
    st.markdown('* **decade:** Periodo de decada (periodo de 10 anos).')
    st.markdown('* **imdb_bucket:** Média de avaliação IMDB.')
    st.markdown('* **genres:** Referece ao gênero do filme ou série, a várias colunas de gênero cada uma para ação, comedia, romance e etc. Essas colunas recebem valores de 0 (False) é 1 (True) para o gênero pertencido.')
    st.markdown('* **platforms:** Referece a plataforma em que o filme e série se encontra, no mesmo modelo da coluna "genres" são várias colunas com nomes de plataformas onde recem valores de verdadeiro e falso para cada caso.')

    st.subheader("Lista de Colunas:")
    st.write(df.columns.tolist())