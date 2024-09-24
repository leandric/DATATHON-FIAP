import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import missingno as msno
import matplotlib.pyplot as plt


# Configura o layout para widescreen
st.set_page_config(page_title="Aplicação Widescreen", layout="wide")

df = pd.read_csv('https://raw.githubusercontent.com/leandric/DATATHON-FIAP/refs/heads/main/data/base_tratada.csv')
df_original = pd.read_csv('https://raw.githubusercontent.com/leandric/DATATHON-FIAP/refs/heads/main/data/PEDE_PASSOS_DATASET_FIAP.csv', sep=';')


# Cria as abas
tab1, tab2, tab3, tab4 = st.tabs(["Introdução", "Tratamento e Modelagem dos Dados", "Segmentação de Alunos", "Tendencias e Conclusões"])

# Conteúdo da Aba 1
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('''
            ## Transformando Vidas com a Associação Passos Mágicos
            Imagine um lugar onde crianças e jovens em situação de vulnerabilidade social encontram esperança e oportunidades para brilhar. Desde 1992, a Associação Passos Mágicos, fundada por Michelle Flues e Dimetri Ivanoff, tem sido esse lugar em Embu-Guaçu. O que começou em orfanatos se transformou, ao longo de 30 anos, em uma ampla gama de programas que oferecem educação de qualidade, suporte psicológico e um espaço para o desenvolvimento integral.
                    
            
            Com uma missão voltada para o desenvolvimento integral, a Associação prepara os jovens para serem protagonistas de suas próprias histórias, oferecendo oportunidades que vão além da sala de aula. Entre os programas oferecidos, destacam-se o apadrinhamento de jovens, intercâmbios culturais e eventos sociais, que incentivam a construção de uma comunidade mais empática e solidária. Através de seus valores centrais, como a empatia e o amor ao aprendizado, a ONG busca criar um ambiente onde todos possam desenvolver seu potencial.
            ''')
        st.markdown('''
        ## Sobre o Conjunto de Dados
Este trabalho se baseia no conjunto de dados e métricas utilizados nas pesquisas do PEDE (Pesquisa Extensiva do Desenvolvimento Educacional) realizadas pela ONG Passos Mágicos nos anos de 2020, 2021 e 2023. Os dados foram coletados pela própria ONG, e as métricas foram desenvolvidas por Dario Rodrigues Silva em parceria com a Passos Mágicos. Esses dados são fundamentais para avaliar o impacto das iniciativas da ONG e compreender a eficácia de suas intervenções ao longo do tempo.
    ''')
        

    with col2:
        st.image('https://yt3.googleusercontent.com/ytc/AIdro_kaSHgX8JGIyURw6ag9sMFtLB_QxMcYWiBOU_4ttvgfKQ=s900-c-k-c0x00ffffff-no-rj',
                 width=800)




# Conteúdo da Aba 2
with tab2:
    
    # Cria o gráfico com missingno
    fig, ax = plt.subplots()
    msno.matrix(df_original, ax=ax)  # Gera o gráfico no 'ax'
    ax.set_yticklabels([])

    col1, col2 = st.columns(2)

    with col1:
        st.header("Modelagem e Análise Exploratória de dados")
        st.markdown('''Inicialmente, estudamos o [Dicionário de Dados do Datathon](https://github.com/leandric/DATATHON-FIAP/blob/main/Dicion%C3%A1rio%20Dados%20Datathon.pdf) para compreender melhor a estrutura e os dados disponíveis. Durante essa análise, observamos que a base de dados utiliza a repetição de colunas para cada ano, o que não seria ideal para conduzir análises robustas. Esse layout resulta em um número elevado de dados nulos nas colunas repetidas. Com isso em mente, realizamos uma análise focada na identificação e tratamento desses dados ausentes.''')
        st.markdown('A base de dados apresenta lacunas em diversas áreas, o que é evidenciado pela presença de três blocos distintos no gráfico. Essa característica está alinhada com a estrutura do conjunto de dados, onde colunas equivalentes são repetidas para cada ano. Isso resulta em uma quantidade significativa de valores ausentes em certas colunas, enquanto outras apresentam dados completos.')
    
    with col2:
        st.pyplot(fig)

    st.markdown('## Transformando a base')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('''
            Para otimizar a análise e aprimorar a qualidade das visualizações, decidimos segmentar 
            a base de dados em três subconjuntos, correspondentes a cada ano. Essa abordagem facilita a 
            padronização dos nomes das colunas e a uniformização da estrutura dos dados. Após o tratamento individual de 
            cada subconjunto, realizamos o merge das bases, o que nos permitiu avançar de forma eficiente com a análise exploratória.
        ''')

    with col2:
        with st.expander('Base de dados tratada'):
            st.markdown('''
        
        | Coluna                          | Tipo de Dado        |
        |----------------------------------|---------------------|
        | INSTITUICAO_ENSINO_ALUNO         | object              |
        | IDADE_ALUNO                      | object              |
        | ANOS_PM                          | object              |
        | FASE_TURMA                       | object              |
        | PONTO_VIRADA                     | object              |
        | INDE                             | float64             |
        | INDE_CONCEITO                    | object              |
        | PEDRA                            | object              |
        | DESTAQUE_IEG                     | object              |
        | DESTAQUE_IDA                     | object              |
        | DESTAQUE_IPV                     | object              |
        | IAA                              | object              |
        | IEG                              | object              |
        | IPS                              | object              |
        | IDA                              | object              |
        | IPP                              | object              |
        | IPV                              | object              |
        | IAN                              | object              |
        | NOME                             | object              |
        | ano                              | object              |
        | FASE                             | float64             |
        | TURMA                            | object              |
        | SINALIZADOR_INGRESSANTE          | object              |
        | REC_EQUIPE_1                     | object              |
        | REC_EQUIPE_2                     | object              |
        | REC_EQUIPE_3                     | object              |
        | REC_EQUIPE_4                     | object              |
        | NIVEL_IDEAL                      | object              |
        | DEFASAGEM                        | float64             |
        | ANO_INGRESSO                     | float64             |
        | BOLSISTA                         | object              |
        | CG                               | float64             |
        | CF                               | float64             |
        | CT                               | float64             |
        | NOTA_PORT                        | float64             |
        | NOTA_MAT                         | float64             |
        | NOTA_ING                         | float64             |
        | QTD_AVAL                         | float64             |
        | REC_AVA_1                        | object              |
        | REC_AVA_2                        | object              |
        | REC_AVA_3                        | object              |
        | REC_AVA_4                        | object              |
        | INDICADO_BOLSA                   | object              |
        | ANO                              | datetime64[ns]      |
        ''')
      
    with col3:
        with st.expander('Base de dados original'):
            st.markdown('''
             
        | Coluna                          | Tipo de Dado |
        |----------------------------------|--------------|
        | INSTITUICAO_ENSINO_ALUNO_2020    | object       |
        | NOME                             | object       |
        | IDADE_ALUNO_2020                 | object       |
        | ANOS_PM_2020                     | object       |
        | FASE_TURMA_2020                  | object       |
        | PONTO_VIRADA_2020                | object       |
        | INDE_2020                        | object       |
        | INDE_CONCEITO_2020               | object       |
        | PEDRA_2020                       | object       |
        | DESTAQUE_IEG_2020                | object       |
        | DESTAQUE_IDA_2020                | object       |
        | DESTAQUE_IPV_2020                | object       |
        | IAA_2020                         | object       |
        | IEG_2020                         | object       |
        | IPS_2020                         | object       |
        | IDA_2020                         | object       |
        | IPP_2020                         | object       |
        | IPV_2020                         | object       |
        | IAN_2020                         | object       |
        | FASE_2021                        | float64      |
        | TURMA_2021                       | object       |
        | INSTITUICAO_ENSINO_ALUNO_2021    | object       |
        | SINALIZADOR_INGRESSANTE_2021     | object       |
        | PEDRA_2021                       | object       |
        | INDE_2021                        | object       |
        | IAA_2021                         | float64      |
        | IEG_2021                         | float64      |
        | IPS_2021                         | float64      |
        | IDA_2021                         | float64      |
        | IPP_2021                         | float64      |
        | REC_EQUIPE_1_2021                | object       |
        | REC_EQUIPE_2_2021                | object       |
        | REC_EQUIPE_3_2021                | object       |
        | REC_EQUIPE_4_2021                | object       |
        | PONTO_VIRADA_2021                | object       |
        | IPV_2021                         | float64      |
        | IAN_2021                         | float64      |
        | NIVEL_IDEAL_2021                 | object       |
        | DEFASAGEM_2021                   | float64      |
        | FASE_2022                        | float64      |
        | TURMA_2022                       | object       |
        | ANO_INGRESSO_2022                | float64      |
        | BOLSISTA_2022                    | object       |
        | INDE_2022                        | float64      |
        | CG_2022                          | float64      |
        | CF_2022                          | float64      |
        | CT_2022                          | float64      |
        | PEDRA_2022                       | object       |
        | DESTAQUE_IEG_2022                | object       |
        | DESTAQUE_IDA_2022                | object       |
        | DESTAQUE_IPV_2022                | object       |
        | IAA_2022                         | float64      |
        | IEG_2022                         | float64      |
        | IPS_2022                         | float64      |
        | IDA_2022                         | float64      |
        | NOTA_PORT_2022                   | float64      |
        | NOTA_MAT_2022                    | float64      |
        | NOTA_ING_2022                    | float64      |
        | QTD_AVAL_2022                    | float64      |
        | IPP_2022                         | float64      |
        | REC_AVA_1_2022                   | object       |
        | REC_AVA_2_2022                   | object       |
        | REC_AVA_3_2022                   | object       |
        | REC_AVA_4_2022                   | object       |
        | INDICADO_BOLSA_2022              | object       |
        | PONTO_VIRADA_2022                | object       |
        | IPV_2022                         | float64      |
        | IAN_2022                         | float64      |
        | NIVEL_IDEAL_2022                 | object       |
        ''')

    col1, col2 = st.columns(2)

    with col1:
        pass

    with col2:
        # Converter a coluna 'INDE' para valores numéricos (forçando erros para NaN)
        df['INDE'] = pd.to_numeric(df['INDE'], errors='coerce')

        # Remover linhas onde 'INDE' ou 'ano' tenham valores ausentes (NaN)
        df_clean = df.dropna(subset=['INDE', 'ano'])

        # Filtrar para mostrar apenas os anos 2020, 2021 e 2022
        df_filtered = df_clean[df_clean['ano'].isin([2020, 2021, 2022])]

        # Agrupar por 'ano' e calcular a média do INDE
        df_grouped = df_filtered.groupby('ano')['INDE'].mean().reset_index()

        # Criar o gráfico de colunas (barras) usando Matplotlib com cor azul pastel
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(df_grouped['ano'], df_grouped['INDE'], color='#AEC6CF')

        # Adicionar título e rótulos
        ax.set_title('Média do Índice de Desenvolvimento Educacional ao Longo dos Anos (2020-2022)')
        ax.set_xlabel('Ano')

        # Remover os números do eixo Y
        ax.set_yticks([])

        # Adicionar rótulos nas barras
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

        # Ajustar os ticks do eixo X para mostrar apenas os anos 2020, 2021 e 2022
        ax.set_xticks([2020, 2021, 2022])

        # Remover a legenda (caso haja)
        ax.legend().set_visible(False)

        # Mostrar o gráfico no Streamlit
        st.pyplot(fig)

        ##############################################################
        # Converter a coluna 'IEG' para valores numéricos (forçando erros para NaN)
        df['IEG'] = pd.to_numeric(df['IEG'], errors='coerce')

        # Remover linhas onde 'IEG' ou 'ano' tenham valores ausentes (NaN)
        df_clean = df.dropna(subset=['IEG', 'ano'])

        # Filtrar para mostrar apenas os anos 2020, 2021 e 2022
        df_filtered = df_clean[df_clean['ano'].isin([2020, 2021, 2022])]

        # Agrupar por 'ano' e calcular a média do IEG
        df_grouped = df_filtered.groupby('ano')['IEG'].mean().reset_index()

        # Criar o gráfico de colunas (barras) usando Matplotlib com cor azul pastel
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(df_grouped['ano'], df_grouped['IEG'], color='#AEC6CF')

        # Adicionar título e rótulos
        ax.set_title('Média do Indicador de Engajamento ao Longo dos Anos (2020-2022)')
        ax.set_xlabel('Ano')

        # Remover os números do eixo Y
        ax.set_yticks([])

        # Adicionar rótulos nas barras
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

        # Ajustar os ticks do eixo X para mostrar apenas os anos 2020, 2021 e 2022
        ax.set_xticks([2020, 2021, 2022])

        # Remover a legenda (caso haja)
        ax.legend().set_visible(False)

        # Mostrar o gráfico no Streamlit
        st.pyplot(fig)
        ###################################################################################
        # Converter a coluna 'IDA' para valores numéricos (forçando erros para NaN)
        df['IDA'] = pd.to_numeric(df['IDA'], errors='coerce')

        # Remover linhas onde 'IDA' ou 'ano' tenham valores ausentes (NaN)
        df_clean = df.dropna(subset=['IDA', 'ano'])

        # Filtrar para mostrar apenas os anos 2020, 2021 e 2022
        df_filtered = df_clean[df_clean['ano'].isin([2020, 2021, 2022])]

        # Agrupar por 'ano' e calcular a média do IDA
        df_grouped = df_filtered.groupby('ano')['IDA'].mean().reset_index()

        # Criar o gráfico de colunas (barras) usando Matplotlib com cor azul pastel
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(df_grouped['ano'], df_grouped['IDA'], color='#AEC6CF')

        # Adicionar título e rótulos
        ax.set_title('Média do Indicador de Aprendizagem ao Longo dos Anos (2020-2022)')
        ax.set_xlabel('Ano')

        # Remover os números do eixo Y
        ax.set_yticks([])

        # Adicionar rótulos nas barras
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

        # Ajustar os ticks do eixo X para mostrar apenas os anos 2020, 2021 e 2022
        ax.set_xticks([2020, 2021, 2022])

        # Remover a legenda (caso haja)
        ax.legend().set_visible(False)

        # Mostrar o gráfico no Streamlit
        st.pyplot(fig)
        ###########################################################################
        # Converter a coluna 'IPV' para valores numéricos (forçando erros para NaN)
        df['IPV'] = pd.to_numeric(df['IPV'], errors='coerce')

        # Remover linhas onde 'IPV' ou 'ano' tenham valores ausentes (NaN)
        df_clean = df.dropna(subset=['IPV', 'ano'])

        # Filtrar para mostrar apenas os anos 2020, 2021 e 2022
        df_filtered = df_clean[df_clean['ano'].isin([2020, 2021, 2022])]

        # Agrupar por 'ano' e calcular a média do IPV
        df_grouped = df_filtered.groupby('ano')['IPV'].mean().reset_index()

        # Criar o gráfico de colunas (barras) usando Matplotlib com cor azul pastel
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(df_grouped['ano'], df_grouped['IPV'], color='#AEC6CF')

        # Adicionar título e rótulos
        ax.set_title('Média do Indicador de Ponto de Virada ao Longo dos Anos (2020-2022)')
        ax.set_xlabel('Ano')

        # Remover os números do eixo Y
        ax.set_yticks([])

        # Adicionar rótulos nas barras
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

        # Ajustar os ticks do eixo X para mostrar apenas os anos 2020, 2021 e 2022
        ax.set_xticks([2020, 2021, 2022])

        # Remover a legenda (caso haja)
        ax.legend().set_visible(False)

        # Mostrar o gráfico no Streamlit
        st.pyplot(fig)
        #################################################
        # Selecionar as colunas de interesse: IEG, IDA, INDE, IPV
        df_filtered = df[['IEG', 'IDA', 'INDE', 'IPV']].dropna()

        # Calcular a matriz de correlação
        correlation_matrix = df_filtered.corr()

        # Criar o heatmap de correlação usando Seaborn
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)

        # Adicionar título
        ax.set_title('Matriz de Correlação entre IEG, IDA, INDE e IPV')

        # Mostrar o gráfico no Streamlit
        st.pyplot(fig)


# Conteúdo da Aba 3
with tab3:
    st.header("Conteúdo da Aba 3")
    st.write("Este é o conteúdo da terceira aba.")

# Conteúdo da Aba 4
with tab4:
    st.header("Conteúdo da Aba 4")
    st.write("Este é o conteúdo da quarta aba.")



# Barra lateral para navegação ou informações adicionais
st.sidebar.title("Menu")
st.sidebar.markdown("Selecione as opções abaixo:")








