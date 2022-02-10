"""
Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor
"""
n = int(input('Digite um número: '))
ant = n - 1
suc = n + 1
print('O antecessor de {} é {} e o sucessor é {}'.format(n, ant, suc))

# Simplificando o codigo
n1 = int(input('Digite um numero: '))
print('O antecessor de {} é {}, e o sucessor é {}'.format(n1, (n1 - 1), (n1 + 1)))