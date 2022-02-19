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

n1 = input('Digite um noméro entre 0 e 9999: ')
print('UNIDADE: {}\n'.format(n1[3]),
      'DEZENA: {}\n'.format(n1[2]),
      'CENTENA: {}\n'.format(n1[1]),
      'MILHAR: {}'.format(n1[0]))