import streamlit as st

# Adicionando um titulo a página (Apenas uma assinatura como forma de identificação)
st.set_page_config(page_title="Pedro Ryan")

#Container 1º, titulo e logo da HBO MAX
with st.container():
    st.title('Análise da Base - HBO MAX')

    #Adicionando o link de um Gif da logo HBO MAX
    gif_url = 'https://images.squarespace-cdn.com/content/v1/52adf1abe4b0dbce9d210136/1604798976116-DX27OWGAXKUYDG9RIDKY/HBO+Max+-+Kutko+Article+GIF.gif?format=2500w'
    st.image(gif_url, use_container_width=True) #Comando para exibir o Gif

#Container 2º, explicando oque a base de dados
with st.container():
    st.title('Oque é a Base da HBO MAX?')
    st.write('A Base da HBO MAX é basicamente uma lista com o catálogo de filmes e séries, onde também está detalhando o seu gênero sendo ação, comedia, romance entre outros mais.')
    st.write('Além dessas informações a base de dados fornece informações de onde mais os filmes e séries estão disponiveis, exemplos de outras plataformas de streaming como "Amazon Prime", "Netflix" e etc.')


    #Adicionando o link de um Gif da plataforma HBO MAX
    gif_url = 'https://images.squarespace-cdn.com/content/v1/52adf1abe4b0dbce9d210136/1604110439985-ZMHFGV7B48XOF35I14I2/HBO+Max+-+Family+Section+GIF.gif?format=2500w'
    st.image(gif_url, use_container_width=True) #Comando para exibir o Gif

    st.subheader('Oque é esse projeto?')
    st.write('Esse projeto faz consultas do catalago da HBO MAX, nessas consultas podem ser filtrados os dados por período de ano, pelo tipo de gênero do programa sendo ação, romance, comédia e etc, também e possível visualizar em quais plataformas os programas estão disponíveis.')
    st.write('Nesse projeto existem gráficos e comparação de críticas de programas onde podem ser filtrados também de acordo com suas necessidades ou preferências.')
    st.write('Outro detalhe do projeto e que ele faz o rank dos melhores programas, junto dessa visualização você pode verificar onde está disponivel esses programas.')
    st.write('Também pode ser visto a média de pontuação da crítica por programa, além de ter essa visualização você pode filtrar a consulta e visualização desses dados pelo ano de lançamento, tipo de gênero é plataforma disponível.')
