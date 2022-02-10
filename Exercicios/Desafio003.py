"""
Desafio
-> Crie um programa que leia dois numeros e mostre a soma entre eles.
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
print('A soma entre {} e {}, é {}.'.format(n1, n2, s))
print('===================================')

# ou

print(f'A soma entre {n1} e {n2} é igual a {s}')
