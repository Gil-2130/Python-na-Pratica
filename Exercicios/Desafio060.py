"""

Faça um programa que leia um número qualquer e mostre seu fatorial
ex; 5! = 5x4x3x2x1 = 120

"""

# Importando módulos para calcular fatorial
from math import factorial

# Soliciando o número para o usuário
n = int(input('Digite um número: '))
f = factorial(n)

print('O fatorial de {} é {}'.format(n, f))


# Resolvendo o problema de forma convencional

# Solicitando um número ao usuário
n = int(input('Digite um número para calcular seu fatorial: '))

# Contador
c = n

# Fatorial
f = 1

# Imprimindo o fatorial
print('Calculando {}! = '.format(n), end='')

# Enquanto o contador for maior que 0
while c > 0:

    # imprimindo c
    print('{} '.format(c), end='')

    # acrescentando "x" á c enquanto este for maior que 1 (deixando o codigo mais legível)
    print('x ' if c > 1 else ' = ', end='')

    # Fatorial (multiplicação de cada elemento de c)
    f = f * c
    
    # Contador subtraindo o valor de n - 1
    c = c - 1
    
print('{}'.format(f))
