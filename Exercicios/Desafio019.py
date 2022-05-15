"""
Um professor quer sortear um dos seus 04 alunos para apagar o quadro.
Faça um programa que o ajude lendo o nome deles e escrevendo o nome do escolhido.
"""


# Importando a biblioteca
from random import choice
# Criando uma tupla para armazenar os nomes
names = 'maria', 'joao', 'pedro', 'gustavo'
# Imprimindo os resultados
print('O nome escolhido foi {}.'.format(choice(names)))


# Resposta do professor
n1 = str(input('Primeiro Aluno? '))
n2 = str(input('Segundo aluno? '))
n3 = str(input('Terceiro aluno? '))
n4 = str(input('Quarto aluno? '))
lista = [n1, n2, n3, n4]

escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
