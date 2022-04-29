"""

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

"""
# Solicitando um número
n = int(input('Digite um número: '))

# variavel para armazenar o total
total = 0

# Laço de repetição
for i in range(1, n + 1):
    
    # Condicional da divisão do input pelo iterador no range
    if n % i == 0:
        print('\033[33m', end='')
        
        # adicionado á variavel
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')

print('\n\033[m0 Número {} foi divisivel {} vezes.'.format(n, total))
if total == 2:
    print('Este é um número primo!')
else:
    print('Este não é um numero primo!')
