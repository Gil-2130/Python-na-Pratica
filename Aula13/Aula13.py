"""
    Trabalhando com Listas
    lista = [] representada por uma variavel armazenando elementos dentro de colchetes
"""

# Exemplos:

# lista de alimentos
lanche = ['hamburguer', 'suco', 'pizza', 'picolé']

# Imprimindo um elemento da lista
print(lanche[2])

# Imprimindo alguns elementos da lista
print(lanche[0::2])

# Imprimindo o último elemento da lista
print(lanche[-1:])

# alterando algum elemento da lista
lanche[3] = 'goiaba'
print(lanche[3])

# Adicionando elementos na lista(será adicionado no final da lista ok?)
lanche.append('bixcoito')
print(lanche)

# Adicionado elementos em determinado index(posição) na lista
lanche.insert(0, 'macarrão')
print(lanche)

# Excluindo elementos da lista (existem vários métodos)

# Método 1
del lanche[2] # note que nesta posição, está o suco. o mesmo será apagado
print(lanche)

# Método 2 (este método remove o último elemento se não for explicitamente especificado)
lanche.pop(2)
print(lanche)

# Método 3 (em vez de indice, usa-se o nome do elemento)
lanche.remove('macarrão')

# Exemplo do "remove" acima
if 'macarrão' in lanche:
    lanche.remove('macarrão')

# Criando uma lista de um range
lista = list(range(3, 10))
print(lista)

# Criando uma lista desordenada e em seguida colocando-a em sequência
lista_1 = [8,3,6,9,4,2,1,10,7,5]
print(f'Lista desordenada:\n{lista_1}')

lista_1.sort()
print(f'Lista Ordenada:\n{lista_1}')

lista_1.sort(reverse=True)
print(f'A lista ordenada em ordem decrescente é:\n{lista_1}')

# Verificando o tipo de dado
print(f'O tipo de dado é: {type(lista_1)}')

# Obtendo o tamanho da lista
print(f'A lista contém {len(lista_1)} elementos.')

# Criando uma lista vazia e em seguida, adicionando valores à mesma:
valores = []
valores.append(5)
valores.append(8)
valores.append(9)
valores.append(10)
print(valores)

# imprimindo os valores e indices da lista
for indice, valor in enumerate(valores):
    print(f'No indice {indice}, está o valor {valor}')

# Criando uma lista usando o for
valores_1 = list()
for cont in range(0,5):
    valores_1.append(int(input('Digite um valor: ')))
print(valores_1)

# Imprimindo a lista
for c, v in enumerate(valores_1):
    print(f'No indice {c}, está o valor {v}')

# trabalhando com listas
a = [2,4,6,8]

# Realizando a cópia da lista criada
b = a[:]
# alterando algum elemento da lista b (apenas para verificar que esta é uma lista independente
b[2] = 8
# Imprimindo os resultados
print(f'Lista A: {a}')
print(f'Lista B: {b}')
