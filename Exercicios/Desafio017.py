"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triangulo retangulo, calcule e mostre o compriento da hipotenusa.
"""

# A minha Resposta
from math import sqrt, trunc
cat_ops = int(input('Qual o valor do cateto oposto?: '))
cat_adj = int(input('Qual é o valor do cateto adjacente? '))
hipo_x = sqrt(pow(cat_ops, 2) + pow(cat_adj, 2))
print('O valor da Hipotenusa é {}'.format(trunc(hipo_x)))
