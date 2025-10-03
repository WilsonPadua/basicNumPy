"""
ANÁLISE E LIMPEZA DE DADOS COM PANDAS

Este codigo demonstra um fluxo de trabalho completo, desde a criacao de dados
brutos e "sujos" até a sua limpeza, tratamento e manipulacao final.
Ele utiliza:
    - criacao e leitura de CSV.
    - Inspeção de DataFrame com .info(), .shape, .columns, .index, .dtypes.
    - Identificação de valores nulos/inexistentes com .isnull().sum().
    - Tratamento de nulos com .dropna() e .fillna() (com diferentes estratégias).
    - Correção de tipos de dados com .astype().
    - Seleção e filtragem de dados com .loc, .iloc e máscaras booleanas.
    - Criação de novas colunas a partir de dados existentes.

Author: João Wilson
"""

import pandas as pd
import numpy as np
import os

#criacao do DF com um arquivo .csv
arquivo_csv = 'dataRaw.csv'
df = pd.read_csv(arquivo_csv, na_values=['N/A'])
#o pandas pode reconhecer automaticamente os valores nulos

#visualizando as primeiras linhas do DF usando a funcao .head()
print("usando a funcao .head para visualizar as primeiras linhas do DF")
print(df.head())

#fazendo a analise de alguns atributos importantes do DF com .shape .index e .columns
print("atributos importantes do DF")
print(f"Formato (Linhas, Colunas): {df.shape}")
print(f"Nomes das Colunas: {df.columns.to_list()}")
print(f"Índice das Linhas: {df.index}")

#contagem total dos valores nulos ou inexistentes por coluna
qtdNulos = df.isnull().sum()

#exibindo as colunas com nulos
print("colunas com valores nulos")
print(qtdNulos[qtdNulos > 0])


#inicio do tratamento dos dados

#criando uma copia para tratar os dados e comparar no final
data = df.copy()

#tratando a coluna de vendedores
print("tratando os valores invalidos da coluna de vendedor...")
#como o DF tem diferentes tipos de dados, a forma de tratar cada coluna deve ser diferente
#a funcao .fillna() substitui valores nulos sem apagar a coluna
data["Vendedor"] = data["Vendedor"].fillna("Desconhecido")
print("valores invalidos de vendedor substituidos por 'Desconhecido'")

#tratando a coluna de quantidades vendidas
print("tratando os valores invalidos da coluna de quantidade vendida...")
#diferente da coluna de vendedores que tem apenas valores em string, a coluna da quantidade vendida recebe int
data["Quantidade_Vendida"] = data["Quantidade_Vendida"].fillna(-1)
print("valores nao informados preenchidos com -1")

#tratando a coluna de preco unitario
print("tratando os valores invalidos da coluna de preco unitario")
data["Preco_Unitario"] = data["Preco_Unitario"].fillna(-1)
print("valores nao informados preenchidos com -1")

#verificando se ainda existem valores nulos ou invalidos
print("verificacao de valores invalidos no DF tratado")
print(data.isnull().sum())

#ajustes finais e manipulacao dos dados tratados

#mudando a coluna de quantidade vendida de float para int
print("alterando os valores de quantidade vendida de float para int")
data["Quantidade_Vendida"] = data["Quantidade_Vendida"].astype(int)

#informacoes do DF corrigido
print("DataFrame após limpeza e ajustes")
print(data.info())

print("DF corrigido")
print(data)