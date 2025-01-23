import streamlit as st
import pandas as pd
import plotly.express as px

#Container 1º, introdução do que e a análise
with st.container():
    st.title('Análise dos Top 10 Melhores programas')
    st.write('A análise e sobre os melhore programas do catálogo de acordo com sua nota IMDB, logo abaixo eles estão exibidos em ordem de classificação é com suas notas.')
    st.write('Quando passar o mouse por cima da coluna de um dos classificados será mostrado detalhadamente a númeração exata do IMDB junto do título do programa.')
    st.write('Logo após o gráfico de barra tem o um gráfico mostrando quais plataformas esses programas estão disponiveis (quando passar o mouse por cima da colunas), também e possivel ver em quantas plataformas são no total.')
#Container 2º, Exibindo os gráficos
with st.container():
    df = pd.read_csv('HBO-MAX-Content.csv', encoding='ISO-8859-1', sep=';')
    
    df = df.sort_values(by='imdb_score', ascending=False).head(10)

    # Gráfico de barras interativo com Plotly Express
    fig = px.bar(df, x='title', y='imdb_score',
                labels={'title': 'Título', 'imdb_score': 'Média de nota'},
                 title='Top 10 - Programas')
    st.plotly_chart(fig, use_container_width=True)

    # Layout da aplicação
    st.subheader('Quantidades de plataformas que estão disponiveis:')
    st.bar_chart(df.set_index('title')[['platforms_acorntv' ,'platforms_adult_swim_tveverywhere' ,'platforms_amazon_prime' ,'platforms_amc' ,'platforms_amc_premiere' ,'platforms_bbc_america_tve' ,'platforms_britbox' ,'platforms_cartoon_network' ,'platforms_cbs_all_access' ,'platforms_cinemax' ,'platforms_comedycentral_tveverywhere' ,'platforms_criterion_channel' ,'platforms_crunchyroll_premium' ,'platforms_curiositystream' ,'platforms_dc_universe' ,'platforms_epix' ,'platforms_fandor' ,'platforms_free' ,'platforms_fubo_tv' ,'platforms_funimation' ,'platforms_hbo' ,'platforms_hbo_max' ,'platforms_hoopla' ,'platforms_hulu_plus' ,'platforms_kanopy' ,'platforms_nbc_tveverywhere' ,'platforms_netflix' ,'platforms_shoutfactorytv' ,'platforms_showtime' ,'platforms_shudder' ,'platforms_starz' ,'platforms_sundancenow' ,'platforms_syfy_tveverywhere' ,'platforms_tbs' ,'platforms_tnt' ,'platforms_trutv_tveverywhere' ,'platforms_urbanmoviechannel' ,'platforms_velocity_go' ,'platforms_watch_tcm']])

    # Tabela com detalhes
    st.subheader('Detalhes em planilha:')
    st.dataframe(df[['title', 'imdb_score', 'platforms_acorntv' ,'platforms_adult_swim_tveverywhere' ,'platforms_amazon_prime' ,'platforms_amc' ,'platforms_amc_premiere' ,'platforms_bbc_america_tve' ,'platforms_britbox' ,'platforms_cartoon_network' ,'platforms_cbs_all_access' ,'platforms_cinemax' ,'platforms_comedycentral_tveverywhere' ,'platforms_criterion_channel' ,'platforms_crunchyroll_premium' ,'platforms_curiositystream' ,'platforms_dc_universe' ,'platforms_epix' ,'platforms_fandor' ,'platforms_free' ,'platforms_fubo_tv' ,'platforms_funimation' ,'platforms_hbo' ,'platforms_hbo_max' ,'platforms_hoopla' ,'platforms_hulu_plus' ,'platforms_kanopy' ,'platforms_nbc_tveverywhere' ,'platforms_netflix' ,'platforms_shoutfactorytv' ,'platforms_showtime' ,'platforms_shudder' ,'platforms_starz' ,'platforms_sundancenow' ,'platforms_syfy_tveverywhere' ,'platforms_tbs' ,'platforms_tnt' ,'platforms_trutv_tveverywhere' ,'platforms_urbanmoviechannel' ,'platforms_velocity_go' ,'platforms_watch_tcm']])
