# Sistema de Recomendação de Patentes

Este projeto implementa um Sistema de Recomendação de Patentes usando técnicas de processamento de linguagem natural e aprendizado de máquina. O objetivo é fornecer recomendações precisas e relevantes de patentes com base em seus textos descritivos.

## Funcionalidades

O projeto consiste em duas partes:

### Parte 1: Embeddings_Patente.ipynb

O notebook `Embeddings_Patente.ipynb` realiza as seguintes etapas:

- Indicação de um conjunto de dados de publicações de patentes.
- Utilização do endpoint de embeddings do OpenAI para gerar representações vetoriais de alta qualidade para cada texto de patente.
  - Utilização do modelo de incorporação text-embedding-ada-002 fornecido pelo OpenAI para gerar vetores de alta qualidade para cada texto de patente.
  - Aplicação da codificação cl100k_base, que é específica para o modelo de incorporação text-embedding-ada-002.
- Preparação dos dados para análise ou tarefas de aprendizado de máquina posteriores.

### Parte 2: Sugestion_Patente.ipynb

O notebook `Sugestion_Patente.ipynb` realiza as seguintes etapas:

- Carrega o arquivo CSV gerado no notebook da parte 1.
- Implementa um sistema de recomendação que retorna os 5 principais resultados de patentes semelhantes com base nos vetores de embeddings.
- Visualização das patentes utilizando a técnica T-SNE para redução de dimensionalidade, permitindo uma representação visual dos dados.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python necessárias: [lista de bibliotecas utilizadas]

## Como usar

1. Execute o primeiro notebook para gerar os embeddings das patentes.

2. Em seguida, execute o segundo notebook para obter as recomendações de patentes semelhantes e visualizar os resultados.
