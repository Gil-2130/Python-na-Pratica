"""
Faça um programa que leia 03 numeros e mostre qual é o maior e qual é o menor.
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite o ultimo numero: '))

# Verificando o menor valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando o maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Imprimindo os resultados
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
