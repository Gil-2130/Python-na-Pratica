# Trabalhando com strings
frase = 'Curso em video Python'
print(frase)


# Fatiamento
print(frase[9])       # Buscando o indice 9
print(frase[2:12])    # Iniciando de um indice até outro indice
print(frase[9:21:2])  # Iniciando de um indice até outro indice e 'pulando' de 2 em 2.
print(frase[:5])    # Fatiando do inicio até o indice especificado
print(frase[5:])  # Iniciando de um indice e indo até onde a string/texto termina
print(frase[5::2])  # Começa em um indice, vai até o final do texto mas pulando de 2 em 2 caracteres


# Obtendo o tamanho de uma string
print(f'A string contém {len(frase)} caracteres!')
print('A string contém {} caracteres!'.format(len(frase)))


# Contando quantos caracteres aparecem repetidamente dentro de uma frase
print(frase.count('o'))  # quantos caracteres aparecem na string(texto)
print(frase.count('o', 0, 13))  # Quantos caracteres aparecem de um indice a outro
print(frase.upper().count('O'))  # Utilizando dois métodos; coloque tudo em maiusculo e conte quantos 'Ós' tem

# Encontrando um caracter ou uma sequencia de caracteres dentro de uma string
print(frase.find('rs'))  # a saida indica em qual indice está localizado o caracter
print('Curso' in frase)  # Existe curso in frase? resposta booleana (lembre-se que pthon é case-sensitive)



"""
============================ TRNSFORMAÇÃO DE STRINGS===================================
"""

# encontrando e substituindo caracteres dentro de uma string
print(frase.replace('Curso', 'osruc'))  # onde tiver 'Curso', será substituido por outra sentença na saída.

# Capitalizando a frase (Coloca a primeira letra da frase em maiusculo)
print(frase.capitalize())

# colocando todas as letras em maiusculo
print(frase.upper())

# Colocando todas as letras da frase em minusculo
print(frase.lower())

# Coloca todas as primeiras letras das palavras em maiusculo (titulo)
print(frase.title())

"""
Iremos trabalhar agora com remoção de espaços excedentes em strings
ex; espaços duplos ao preencher um cadastro ou coisa parecida,
onde acaba tendo muitos espaços desnecessários e isso atrapalha inclusive
quando for manipular as strings em um banco de dados por exemplo...
"""
frase_1 = '   coloquei   03   espaços   '

# Verificando o tamanho da frase
print(len(frase_1))  # 29 caracteres

# removendo todos os espaços (Apenas do inicio e fim da frase)
print(len(frase_1.strip()))  # 23 caracteres

# Viu só?


# De forma similar, podemos remover apenas os espaços á direita da frase (right strip)
print(frase_1.rstrip())

# Removendo espaços á esquerda da frase
print(frase_1.lstrip())

# removendo todos os espaços em excesso
print(len(frase_1.replace('   ', ' ')))


"""
=============== DIVIDINDO A STRING ===========================
"""
# Ao usar o método split, a frase será desempacotada em uma lista de strings
print(frase.split())

# Verificando o tamanho da lista criada
print('A lista possui', len(frase.split()), 'ELEMENTOS')

# Vamos salvar a lista acima em uma variavel
f1 = frase.split()
print(f1)
print(f1[2][3])  # Imprimindo o elemento no indide 02 da lista e o indice 3 desse elemento

# Agora iremos pegar a lista criada acima e concatenar os elementos
f2 = '-'.join(f1)  # Você pode usar qualquer caracter para fazer a concatenação dos elementos da lista
print(f2)
