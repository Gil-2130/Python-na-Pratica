"""
Crie um programa que vai gerar 05 numeros aleatorios
e colocar em uma tupla.

Depois disso mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
"""

# Biblioteca para gerar números aleatórios
from random import randint

# criando numeros aleatórios e colocando em tupla
num = (randint(0, 10), randint(0, 10), randint(0, 10),
     randint(0, 10), randint(0, 10))

# Imprimindo os valores sorteados
print('Os valores sorteados foram: ')
# laço em cada valor da lista
for i in num:
    print(i)

# Imprimindo o maior valor
print(f'O maior valor é: {max(num)}')

# Imprimindo o menor valor
print(f'O menor valor é: {min(num)}')
