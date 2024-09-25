import streamlit as st
import pickle
import numpy as np

# Título da aplicação
st.title("Previsor de Impacto - Projeto Deep Learning")

# Carregar o modelo
with open('modelos/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Carregar o scaler
with open('modelos/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Carregar o label_encoder
with open('modelos/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Função para predição
def fazer_predicao(pedra, ieg, ips, ipp, ida, iaa, ian, model, scaler, label_encoder):
    # Estruturar os dados de entrada
    input_data = np.array([[pedra, ieg, ips, ipp, ida, iaa, ian]])
    
    # Transformar a coluna 'PEDRA' com o LabelEncoder
    input_data[:, 0] = label_encoder.transform(input_data[:, 0])
    
    # Escalar os dados de entrada
    input_data_scaled = scaler.transform(input_data)
    
    # Fazer a predição usando o modelo treinado
    predicao = model.predict(input_data_scaled)
    
    # Retornar o valor da predição
    return "Sim" if predicao[0] > 0.5 else "Não"

# Interface para o usuário
pedra = st.selectbox("Selecione o valor de PEDRA", label_encoder.classes_)
ieg = st.number_input("Insira o valor de IEG", min_value=0.0, max_value=10.0, step=0.1)
ips = st.number_input("Insira o valor de IPS", min_value=0.0, max_value=10.0, step=0.1)
ipp = st.number_input("Insira o valor de IPP", min_value=0.0, max_value=10.0, step=0.1)
ida = st.number_input("Insira o valor de IDA", min_value=0.0, max_value=10.0, step=0.1)
iaa = st.number_input("Insira o valor de IAA", min_value=0.0, max_value=10.0, step=0.1)
ian = st.number_input("Insira o valor de IAN", min_value=0.0, max_value=10.0, step=0.1)

# Botão para fazer a predição
if st.button("Fazer Predição"):
    resultado = fazer_predicao(pedra, ieg, ips, ipp, ida, iaa, ian, model, scaler, label_encoder)
    st.write(f"Resultado da Predição: {resultado}")