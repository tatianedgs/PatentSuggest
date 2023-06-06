# Sistema de Recomendação de Patentes 💡🔍

Este projeto implementa um Sistema de Recomendação de Patentes usando técnicas de processamento de linguagem natural e aprendizado de máquina. O objetivo é fornecer recomendações precisas e relevantes de patentes com base em seus textos descritivos.

## Funcionalidades 🚀

O projeto consiste em duas partes:

### Parte 1: Embeddings_Patente.ipynb

O notebook `Embeddings_Patente.ipynb` realiza as seguintes etapas:

- Indicação de um conjunto de dados de publicações de patentes.
- Utilização do endpoint de embeddings do OpenAI para gerar representações vetoriais de alta qualidade para cada texto de patente. ✨
  - Utilização do modelo de incorporação `text-embedding-ada-002` fornecido pelo OpenAI para gerar vetores de alta qualidade para cada texto de patente.
  - Aplicação da codificação `cl100k_base`, que é específica para o modelo de incorporação `text-embedding-ada-002`.
- Preparação dos dados para análise ou tarefas de aprendizado de máquina posteriores.

### Parte 2: Sugestion_Patente.ipynb

O notebook `Sugestion_Patente.ipynb` realiza as seguintes etapas:

- Carrega o arquivo CSV gerado no notebook da parte 1.
- Implementa um sistema de recomendação que retorna os 5 principais resultados de patentes semelhantes com base nos vetores de embeddings. 🎯
- Visualização das patentes utilizando a técnica T-SNE para redução de dimensionalidade, permitindo uma representação visual dos dados. 🌐

## Requisitos ✅

- Python 3.7 ou superior
- Bibliotecas Python necessárias: [lista de bibliotecas utilizadas]

## Como usar 📚

1. Execute o primeiro notebook (`Embeddings_Patente.ipynb`) para gerar os embeddings das patentes.

2. Em seguida, execute o segundo notebook (`Sugestion_Patente.ipynb`) para obter as recomendações de patentes semelhantes e visualizar os resultados.

## Exemplo de Resultado 📷

![Exemplo de Recomendação1](./image/IMG1.PNG)
![Exemplo de Recomendação2](./image/IMG2.PNG)

## Aplicação: Sistema de Recomendação de Patente

O sistema também inclui uma aplicação interativa desenvolvida com o Streamlit. A aplicação permite realizar consultas e receber recomendações de patentes semelhantes. Veja como usar:

1. Abra o terminal ou prompt de comando.

2. Crie um novo ambiente virtual usando o Conda com o seguinte comando:

```conda create --name nome_do_ambiente python=3.9```

3. Ative o ambiente virtual recém-criado com o seguinte comando:

```conda activate nome_do_ambiente```

4. Navegue até o diretório raiz do projeto:

```cd caminho/para/o/diretorio```

5. Instale as dependências do projeto:

```pip install -r requirements.txt```

6. Execute a aplicação com o seguinte comando:

`streamlit run Aplicacao.py`.

 -  Pode acessar também a aplicação no seu navegador no endereço `http://localhost:8501`.

## Contribuição 👥

Contribuições são bem-vindas! 🤝

## Licença 📝

Este projeto é licenciado sob a [Licença MIT](LICENSE).
