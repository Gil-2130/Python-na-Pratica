"""
Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou ímpar
"""

num = int(input('Digite um numero: '))
if num % 2 == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é ímpar!'.format(num))
