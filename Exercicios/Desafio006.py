"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e Raís quadrada
"""
n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** 2
print('O dobro de {} é {}'.format(n, dobro))
print('=' * 20)
print('O Triplo de {} é {}'.format(n, triplo))
print('=' * 20)
print('A Raiz quadrada de {} é {}'.format(n, raiz))