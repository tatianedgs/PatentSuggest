# Sistema de Recomendação de Patentes

Este projeto implementa um Sistema de Recomendação de Patentes usando técnicas de processamento de linguagem natural e aprendizado de máquina. O objetivo é fornecer recomendações precisas e relevantes de patentes com base em seus textos descritivos.

## Funcionalidades

O projeto consiste em duas partes:

### Parte 1: Embeddings_Patente.ipynb

O notebook `Embeddings_Patente.ipynb` realiza as seguintes etapas:

- Fusão das publicações de patentes em um único conjunto de dados.
- Utilização do endpoint de embeddings do OpenAI para gerar representações vetoriais de alta qualidade para cada texto de patente.
- Preparação dos dados para análise ou tarefas de aprendizado de máquina posteriores.

### Parte 2: Sugestion_Patente.ipynb

O notebook `Sugestion_Patente.ipynb` realiza as seguintes etapas:

- Carrega o arquivo CSV gerado no notebook da parte 1.
- Implementa um sistema de recomendação que retorna os 5 principais resultados de patentes semelhantes com base nos vetores de embeddings.
- Apresenta uma visualização de todas as milhares de patentes usando a técnica T-SNE para redução de dimensionalidade.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python necessárias: [lista de bibliotecas utilizadas]

## Como usar

1. Clone este repositório:
