import streamlit as st

# Título da página
st.title("Colegas de Classe - Projeto")

# Dados dos colegas
colegas = [
    {"nome": "Maria Silva", "ra": "12345", "imagem": "https://conteudo.imguol.com.br/c/entretenimento/80/2017/04/25/a-atriz-zoe-saldana-como-neytiri-em-avatar-1493136439818_v2_3x4.jpg", "linkedin": "https://linkedin.com/in/maria", "instagram": "https://instagram.com/maria"},
    {"nome": "João Souza", "ra": "67890", "imagem": "https://conteudo.imguol.com.br/c/entretenimento/80/2017/04/25/a-atriz-zoe-saldana-como-neytiri-em-avatar-1493136439818_v2_3x4.jpg", "linkedin": "https://linkedin.com/in/joao", "instagram": "https://instagram.com/joao"},
    {"nome": "Ana Pereira", "ra": "11223", "imagem": "https://conteudo.imguol.com.br/c/entretenimento/80/2017/04/25/a-atriz-zoe-saldana-como-neytiri-em-avatar-1493136439818_v2_3x4.jpg", "linkedin": "https://linkedin.com/in/ana", "instagram": "https://instagram.com/ana"}
]

# Exibindo informações
for colega in colegas:
    st.image(colega["imagem"], caption=colega["nome"], width=150)
    st.write(f"**Nome:** {colega['nome']}")
    st.write(f"**RA:** {colega['ra']}")
    st.write(f"[LinkedIn]({colega['linkedin']}) | [Instagram]({colega['instagram']})")
    st.write("---")

# Rodar o streamlit usando: streamlit run nome_do_arquivo.py