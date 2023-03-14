import streamlit as st
import pandas as pd

# Define a largura da coluna da imagem e da coluna do formulário
col1, col2 , col3= st.columns([2,0.5,3])

# Adiciona a imagem na primeira coluna
with col1:
    img_url = 'https://cdn.static.linkr.bio/thumb/250x250/cover/85/user/upload/image/101f2c7f-db08-4426-9c57-f31f2ba55974.jpg?f=webp'
    st.text("")
    st.text("")
    st.image(img_url, width=150, output_format='png')
    st.write("E-mail: devBittencourt0@gmail.com")
    st.write("25-year-old software developer working on exciting new projects!")
    st.text("Este formulário foi desenvolvido com Python, Streamlit e Pandas para coletar informações de contato, incluindo nome, email e mensagem. As informações são armazenadas em um banco de dados de forma segura e serão utilizadas de acordo com a política de privacidade estabelecida. O formulário é fácil de usar e intuitivo para os usuários.")
with col2:    
    st.write("")



  
# Adiciona o formulário na segunda coluna
with col3:
    # Define o título da página
    st.title("Contato devBittencourt")
  
    # Define os campos do formulário
    name = st.text_input("Nome")
    email = st.text_input("E-mail")
    message = st.text_area("Mensagem")

    # Cria um botão para enviar o formulário
    btn = st.button("Enviar")

    # Verifica se o botão foi pressionado
    if btn:
        # Cria um dicionário com os dados do formulário
        data = {
            "Nome": name,
            "E-mail": email,
            "Mensagem": message
        }

        # Converte o dicionário em um DataFrame do pandas
        df = pd.DataFrame.from_dict([data])

        # Salva os dados do formulário em um arquivo CSV
        df.to_csv("contatos.csv", index=False)

        # Mostra uma mensagem de confirmação
        st.success("O formulário foi enviado com sucesso!")

