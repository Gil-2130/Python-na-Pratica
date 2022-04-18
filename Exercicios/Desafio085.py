"""
Crie um programa onde o usuário possa digitar 07 valores
numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.

"""

valor = list()

par = list()
impar = list()

for i in range(0, 8):
    v = int(input('Digite um valor: '))
    valor.append(v)

    if v % 2 == 0:
        par.append(v)

    else:
        impar.append(v)

print(f'Os valores pares da lista são {par}.')
print(f'Os valores ímpares da lista são {impar.sort()}.')
