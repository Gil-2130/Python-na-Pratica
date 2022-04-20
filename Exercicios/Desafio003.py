"""
Desafio
-> Crie um programa que leia dois numeros e mostre a soma entre eles.
"""
# Variável para armazenar um número
n1 = int(input('Digite um número: '))
# Variável para armazenar o segundo valor
n2 = int(input('Digite outro numero: '))
# Realizando a soma das duas variáveis
s = n1 + n2
# Imprimindo os resultados
print('A soma entre {} e {}, é {}.'.format(n1, n2, s))
print('===================================')

# ou

print(f'A soma entre {n1} e {n2} é igual a {s}')
