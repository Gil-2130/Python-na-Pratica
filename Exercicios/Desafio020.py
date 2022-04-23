"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho
dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

# Importando biblioteca
import random  # Podmos apenas importar o SHUFFLE -> from random import shuffle
# Criando variaveis para os nomes
n1 = str(input('Primeiro nome? '))
n2 = str(input('Segundo nome? '))
n3 = str(input('Terceiro nome? '))
n4 = str(input('Quarto nome? '))
lista = [n1, n2, n3, n4]
# Obtendo aleatoriamente algum dos nomes
random.shuffle(lista)

print(f'A ordem de apresentação é {lista}')
