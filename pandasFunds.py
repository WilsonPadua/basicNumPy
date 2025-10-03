import pandas as pd
import numpy as np
import os 


#Criacao de Data Frame com pandas
data = {"nome": ["Ana", "Bruno", "Carlos"], "idade":[23,35,42], "cidades":["monteiro", "castanhal", "campina grande"]}
df = pd.DataFrame(data)
print("criacao de um data frame usando dicionario")
print(df)

#criacao de um DF com apenas uma dimensao, utilizando a funcao pd.Series
print("criando um DF unidimensional usando pd.Series e acessando com slice")
s = pd.Series([10,20,30], index=['a','b','c'])

#acesso ao DF com slice
print(s['b'])

#criacao de um DF com arquivo csv
print("criando um DF a partir de um arquivo csv")
arquivo_csv = 'dados.csv'
df.to_csv(arquivo_csv, index=False)

#Leitura do arquivo csv
dataFrame = pd.read_csv(arquivo_csv)
print(dataFrame)
os.remove(arquivo_csv)

#outra forma de criar um DF usando numpy
print("criando a partir de um array NumPy")
dados_numpy = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
#nomeando as colunas do DF na funcao de criacao
df_numpy = pd.DataFrame(dados_numpy, columns=['Coluna_A', 'Coluna_B', 'Coluna_C'])
print(df_numpy)


#propriedades do DF em pandas
print("DF padrao para demostracao das propriedades")
print(df_numpy)

#verificar a quantidade de linhas e colunas, a funcao retorna uma tupla, (nlinhas, ncolunas)
print("Funcao shape")
print(df_numpy.shape)

#retorna os dados das COLUNAS
print("nome das colunas")
print(df_numpy.columns)

#para pegar os indices das linhas e necessario identificar na criacao do DF
df_numpy = pd.DataFrame(dados_numpy, columns=['Coluna_A', 'Coluna_B', 'Coluna_C'], index=['Linha_A', 'Linha_B', 'Linha_C'])
#retorna os indices das LINHAS
print("nome das colunas")
print(df_numpy.index)

#existem duas principais formas de usar as linhas de um DF, .loc[], .iloc[]
#.iloc[] utiliza o indicie numerico assim como em um array normal
print("acesso a linha pelo indicie numerico")
print(df_numpy.iloc[0])

#.loc[] utiliza o nome passado no construtor do DF
print("acesso a linha pelo nome")
print(df_numpy.loc['Linha_A'])


#########################################################################
#Saiba +
#existe uma forma de acessar uma representacao do DF como um array np
print("valores do DF como array NumPy")
print(df.values)
#########################################################################

#operacoes com DF's
data = "data.csv"
df1 = pd.read_csv(data)
print("DF padrao")
print(df1)

#selecinar uma coluna
print("selecionando uma unica coluna")
print(df1['nome'])
#selecionar uma unica coluna gera um pd.Series

#selecionando mais de uma coluna
print("selecionando mais de uma coluna")

subdf = df1[['nome', 'cidade']]
print(subdf)
#selecionar varias colunas gera um DF novo

#selecionar uma linha
print("selecionando uma linha")
print(df1.iloc[0])

#criando uma nova coluna com atraves de uma operacao
print("criando uma coluna idade em meses, multiplicando a coluna das idades por 12")
df1['idade em meses'] = df1['idade'] *12
print(df1)