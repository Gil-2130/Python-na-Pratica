"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos digitos separados.
EX;
Digite um numero: 1834
UNIDADE : 4
DEZENA : 3
CENTENA: 8
MILHAR: 1
"""

n1 = int(input('Digite um numéro entre 0 e 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('UNIDADE: {}'.format(u))
print('DEZENA: {}'.format(d))
print('CENTENA: {}'.format(c))
print('MILHAR: {}'.format(m))
