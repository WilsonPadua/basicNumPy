import numpy as np

#criacao de array em np
arr = np.array([[1,2,3,4],
                [5,6,7,8]])

print("criacao do array1")
print(arr)

#verificacao do formato do array
print("shape do array1: ")
print(arr.shape)

#mudanca do shape do array, tendo como unico criterio manter a mesma quantidade de elementos
print("mudanca do shape do array de 2,4 para 4,2")
print(arr.reshape(4,2))

#broadcast (operacoes entre matrizes diferentes)
arr2 = np.array([[1,2,3,4],
                 [5,6,7,8]])
arr3 = np.array([2])
#regra de implementacao do broadcast
'''
1- Uma das dimensoes precisa ser 1, ou ser igual ao array que vai sofrer a operacao
'''
print("soma dos arrays, arr2: ", end=" ")
print(arr2)
print("com o arr3: ", end='')
print(arr3)
print()
print(arr2 + arr3)

##############################################################################################
#Saiba+
#para fazer um array ter apenas uma dimensao existe a funcao flatten e ravel
print("convertendo array bidimensional usando flatten")
print(arr2.flatten())

print("Convertendo com ravel: ")
print(arr2.ravel())

#flatten e uma funcao que tem efeito colateral, diferentemente de ravel que usa uma copia local
##############################################################################################

#utilizacao de slice em np, utiliza o operador ':'
#array[operador\ linha alvo, operador\ coluna alvo][::-1], o segundo colchete e opcional e serve para inverter os valores
arr4 = np.array([[1,2,3,4],
                [5,6,7,8]])
print("criacao do array base")
print(arr4)

#sintaxe basica para pegar apenas uma coluna do array
print("criacao do slice do array com base nas colunas")
arr5 = arr4[:, 0]
print(arr5)

#sintaxe basica para pegar apenas uma linha do array
print("criacao do slice do array com base nas linhas")
arr6 = arr4[0, :]
print(arr6)

#sintaxe para usar o slice com range
print("criacao do slice do array com range")
arr7 = arr4[0:3, 1:3]
print(arr7)

##############################################################################################
#Saiba+ 2
#verificacao dos valores individuais do array em relacao a outro
print("array de verificacao: ")
print(arr)

#verificando quais valores sao maiores que 3 e criando um array com o output
print("buscando valores maiores que 3")
arr8 = arr > 3
print(arr8)

#mudando o tipo do array utilizando a funcao astype()
print("Alterando os valores do array de boolean para binary")
print(arr8.astype(int))
##############################################################################################

