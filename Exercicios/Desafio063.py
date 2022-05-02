"""
Escreva um programa que leia um número n inteiro e mostre na tela os n primeiros
elementos de uma sequência de Fibonacci.

Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

# Separadores e mensagem do programa
print('=' * 30)
print('Sequência de Fibonacci')
print('=' * 30)

# Solicitando os termos para o usuário
n = int(input('Quantos termos deseja mostrar? '))

# Termos pré-selecionados
t1 = 0
t2 = 1

print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')

cont = 3

while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')

    t1 = t2
    t2 = t3
    cont = cont + 1

print(' -> FIM')
