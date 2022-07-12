"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e Raís quadrada
"""

# Obtendo e armazenando o input do usuário
n = int(input('Digite um número: '))

# Variável para armazenar o dobro
dobro = n * 2

# Variável para armazenar o triplo
triplo = n * 3

# variável para armazenar a raíz quadrada
raiz = n ** 2

# Imprimindo os Resultados
print('O dobro de {} é {}'.format(n, dobro))
print('=' * 20)
print('O Triplo de {} é {}'.format(n, triplo))
print('=' * 20)
print('A Raiz quadrada de {} é {}'.format(n, raiz))
