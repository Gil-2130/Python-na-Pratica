"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher
porém utilizando o laço for.
"""

# Obtendo e arazenando o input do usuário
num = int(input('Digite um número e sua tabuada(x) será calculada: '))
# Laço dentro de um range
for i in range(0, 11):
    # d recebe cada elemento do laço dentro de um range
    d = i
    # Cada elemento do laço é multiplicado pelo valor digitado anteriormente
    i = i * num
    # Imprimindo resultados
    print('{} x {} = {}'.format(num, d, i))


# de forma mais simplificada
n = int(input('Digite um número: '))
for i in range(0,11):
    print('{} X {:2} = {}'.format(n, i, n*i))
