import streamlit as st
import openai
import os
import pandas as pd
import numpy as np
from openai.embeddings_utils import get_embedding, cosine_similarity
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import PDF.Pergunte_PDF as ppdf

st.markdown(
    """
    <h1 style='text-align: center; color: #FFB6C1;'>SISTEMA DE RECOMENDAÇÃO DE PATENTE</h1>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.sidebar.title('🤗 Obrigado por utilizar nossa aplicação!')

    st.sidebar.markdown(
        '<h2 style="text-align: center;">Sobre o Sistema</h2>', unsafe_allow_html=True)
    st.markdown("""
        Feito por Tatiane Santos ([LinkedIn](linkedin.com/in/tatiane-santos-31b79938)) e Evelyn Cristina ([LinkedIn](https://br.linkedin.com/in/evelynlima02))

        Mais informações e o código fonte podem ser encontrados [aqui](https://github.com/tatianedgs/PatentSuggest/blob/main/Aplicacao.py)

        <sub><sup>OBS: Este sistema é uma Prova de Conceito e pode conter erros.<sub><sup>
    """, unsafe_allow_html=True)


paginaSelecionada = st.sidebar.selectbox(
    'Selecione uma Opção', ['Sugestão de Patente', 'Pergunte ao PDF'])

if paginaSelecionada == 'Sugestão de Patente':
    st.title('Sugestão de Patente')

    st.markdown("""
        O objetivo deste sistema é auxiliar na busca por patentes com conteúdo similar, utilizando endpoints e embeddings da OpenAI.
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Carregue a sua base de dados no formato csv:", type='csv')

    if uploaded_file is not None:
        if uploaded_file.size == 0:
            st.error("O arquivo está vazio.")
        else:
            try:
                df = pd.read_csv(uploaded_file)
                if df.columns.empty:
                    st.error("O arquivo não possui colunas.")
                else:
                    st.write(df)
            except pd.errors.EmptyDataError:
                st.error("O arquivo não possui dados.")
            except pd.errors.ParserError:
                st.error(
                    "Erro ao processar o arquivo. Verifique se o formato está correto.")

    # Autenticação

    # **Atenção**: É absolutamente crucial proteger sua chave da OpenAI e compartilhá-la apenas com pessoas autorizadas.
    # Sua chave concede acesso a ferramentas de inteligência artificial extremamente poderosas e, se cair nas mãos erradas,
    # pode ser usada para fins maliciosos. Por favor, tome todas as precauções necessárias para proteger sua chave da OpenAI,
    # incluindo evitar compartilhá-la com qualquer pessoa que não tenha permissão explícita para acessá-la. Lembre-se,
    # proteger sua chave é crucial não apenas para sua própria segurança, mas também para o bem-estar geral da comunidade OpenAI.

    label_text = 'Digite sua chave da API da OpenAI (Atenção: sua chave da OpenAI é privada e não deve ser compartilhada):'
    link_text = 'Obtenha sua chave da API OpenAI'
    link_url = 'https://platform.openai.com/account/api-keys'

    # Configuração da chave da API da OpenAI
    api_key = st.text_input(
        label=f'{label_text} [[{link_text}]]({link_url})', type='password')
    openai.api_key = api_key

    query = st.text_input(
        'Digite um texto ou palavras-chave como fonte para busca de similaridade:', '')

    if st.button('Submeter'):
        run = ((uploaded_file is not None) and (
            api_key is not None) and (query != ''))
        if run:
            try:
                df["embedding"] = df.embedding.apply(eval).apply(np.array)

                # Pesquisa por patentes similares
                def search_patentes(dataframe, patente_description, n=3, pprint=True):
                    df = dataframe.copy()
                    patente_embedding = get_embedding(
                        patente_description, engine="text-embedding-ada-002")
                    df["similarity"] = df.embedding.apply(
                        lambda x: cosine_similarity(x, patente_embedding))
                    results = df.sort_values("similarity", ascending=False).head(
                        n)[['Application Number', 'Title', 'Publication Date', 'URL']]
                    return results

                # Resultados das patentes similares
                result = search_patentes(df, query, 5, False)
                st.write("Resposta:")
                st.write(result)

            except Exception as e:
                st.error("Erro durante o processamento: " + str(e))

elif paginaSelecionada == 'Pergunte ao PDF':
    ppdf.main()
