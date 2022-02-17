"""
Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira
"""

# Usando módulo
from math import trunc
num = float(input('Digite um número real: '))
print('O numero digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))

# Sem usar módulo
print('O número digitadoo foi {} e sua porção inteira é {}'.format(num, int(num)))
