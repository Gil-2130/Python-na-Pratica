"""
Crie um programa que mostre na tela todos os numeros pares que estão no intervalo
entre 1 e 50.
"""

# laço dentro de um range de valores
for lista in range(1, 51):

    # Condicional para imprimir apenas os numeros pares
    if lista % 2 == 0:
        print(lista)

# OU
for n in range(2, 51, 2):
    print(n)
print('FIM')
