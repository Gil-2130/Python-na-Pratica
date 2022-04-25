"""
Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou ímpar
"""

# Obtendo e guardando o input do usuário
num = int(input('Digite um numero: '))
# Condicional para valor par
if num % 2 == 0:
    print('O número {} é par!'.format(num))
# Caso contrário ele é ímpar
else:
    print('O número {} é ímpar!'.format(num))
