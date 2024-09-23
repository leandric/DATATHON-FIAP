import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px



df = pd.read_csv('data/base_tratada.csv')



# Título do app
st.title('Análise de Desempenho dos Alunos - ONG Passos Mágicos')

# Barra lateral para navegação ou informações adicionais
st.sidebar.title("Menu")
st.sidebar.markdown("Selecione as opções abaixo:")



st.markdown('''
## Sobre a ONG 
            
A Associação Passos Mágicos é uma organização sem fins lucrativos fundada em 1992 por Michelle Flues e Dimetri Ivanoff, com o objetivo de transformar a vida de crianças e jovens em situação de vulnerabilidade social. Localizada em Embu-Guaçu, a ONG iniciou suas atividades em orfanatos e, ao longo de 30 anos, expandiu sua atuação para oferecer programas que promovem educação de qualidade, suporte psicológico e atividades diversas que enriquecem a formação de seus beneficiários.

Com uma missão voltada para o desenvolvimento integral, a Associação prepara os jovens para serem protagonistas de suas próprias histórias, oferecendo oportunidades que vão além da sala de aula. Entre os programas oferecidos, destacam-se o apadrinhamento de jovens, intercâmbios culturais e eventos sociais, que incentivam a construção de uma comunidade mais empática e solidária. Através de seus valores centrais, como a empatia e o amor ao aprendizado, a ONG busca criar um ambiente onde todos possam desenvolver seu potencial.
''')

st.markdown('''
## Objetivo da Análise:
entender oimpactando da ONG na vida dos alunos, com base em indicadores de desenvolvimento educacional e engajamento.
''')

st.markdown('''
**Sobre o Conjunto de Dados:** conjunto de dados e métricas utilizados para as Pesquisas do PEDE (Pesquisa Extensiva do Desenvolvimento Educacional) nos anos de 2020, 2021 e 2023, realizadas pela ONG Passos Mágicos. Os dados foram captados pela própria ONG e as métricas foram desenvolvidas por Dario Rodrigues Silva em parceria com a Passos Mágicos.

''')

st.markdown('''
## Perfil dos Estudantes
        
''')

# Contar quantos alunos existem por cada idade
idade_counts = df['IDADE_ALUNO'].value_counts()

# Criando o gráfico
fig, ax = plt.subplots()
idade_counts.sort_index().plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Quantidade de Alunos por Idade')
ax.set_xlabel('Idade')
ax.set_ylabel('Quantidade de Alunos')
ax.grid(True)

# Usar o Streamlit para renderizar o gráfico
st.title('Análise de Idade dos Alunos')
st.pyplot(fig)