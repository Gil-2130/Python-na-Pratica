"""

    tupla = () -> representada com argumentos entre parenteses(não é necessário, mas é uma boa prática)
lista = [] -> REpresentada por argumentos entre colchetes
dicionário = {} -> Representada por elementos dentro de chaves
"""

# Lista ou tupla de Alimentos
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

# Imprimindo os elementos da tupla
print('{:=^40}'.format('Imprimindo a Tupla'))
print(lanche)

# Confirmando o tipo de dado
print('{:=^40}'.format('Confirmando se de fato é uma tupla'))
print(type(lanche))

# Imprimindo algum elemento em específico dentro da tupla
print('{:=^40}'.format('Imprimindo apenas um elemento da tupla(por indice)'))
print(lanche[2])

# Imprimindo apenas alguns elementos da tupla
print('{:=^40}'.format('Imprimindo um range de elementos da tupla'))
print(lanche[0::3])

# Imprimindo de um indice até o final
print('{:=^40}'.format('Imprimindo de determinado elemento até o final'))
print(lanche[1:])

# Imprimindo do inicio até determindado indice
print('{:=^40}'.format('Imprimindo do inicio até determinado elemento(exclusivo)'))
print(lanche[:2])

# Imprimindo o ultimo elemento(quando nãos e sabe qual é o ultimo elemento.
print(lanche[:-1])

# laço de repetição para obter os dados da nossa tupla
print('{:=^40}'.format('Criando um laço e imprimindo os elementos da tupla'))
for c in lanche:
    # Imprimindo apenas as primeiras letras de cada string dentro da tupla
    print('{:=^40}'.format('Imprimindo o elemento e a primeira letra deste elemento'))
    print(c)
    print(c[0])

# Verificando o tamanho da tupla
print('{:=^40}'.format('Verificando o tamanho da TUPLA'))
print(f'A tupla contém {len(lanche)} elementos')

# Obtendo os indices de cada elemento da tupla com o for
print('{:=^40}'.format('Imprimindo os indices da tupla'))
for c in range(0, len(lanche)):
    print(c)

# Imprimindo o indice e o elemento correspondente
print('{:=^40}'.format('Imprimindo o indice e o elemento com o "for"'))
for c in range(0, len(lanche)):
    print(c, lanche[c])

# Usando enumerate para imprimir o indice da tupla
print('{:=^40}'.format('Imprimindo o indice e elemento com o "enumerate"'))
for pos, c in enumerate(lanche):
    print(pos, c)

# Ordenando os elementos da tupla
print('{:=^40}'.format('Imprimindo a tupla ordenada'))
print(sorted(lanche))
# quando fazemos a ordenação, o python transforma a tupla
# Em uma lista em tempo de execução. Ou seja, a tupla não é alterada
print(type(sorted(lanche)))

# COncatenando tuplas
print('{:=^40}'.format('Concatenando Tuplas'))
a = (2, 4, 6)
b = (1, 3, 5)
c = a + b
print(f'Tupla a = {a}')
print(f'Tupla b = {b}')
print(f'Tupla c = {c}')
# Qual o tamanho da tupla? (quantidade de elementos)
print(len(c))
# Quantos vezes um elemento se repete na tupla?
print(c.count(1))
# Em que posição está determinado elemento?
print(c.index(2))
# Obtendo posição de um elemento começando de determinada posição
print(c.index(3, 4))

# Agora iremos confirmar que tuplas são imutáveis

# suponhamos que o indice 2(pizza) da nossa tupla, seja substituído para pão, 
# você acha que seria possível?
lanche[2] = 'Pão'
print(lanche[2])
# Recebemos o seguinte erro:
# TypeError: 'tuple' object does not support item assignment, isto porque não se pode alterar tuplas
