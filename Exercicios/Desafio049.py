"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher
porém utilizando o laço for.
"""

num = int(input('Digite um número e sua tabuada(x) será calculada: '))
for i in range(0, 11):
    d = i
    i = i * num
    print('{} x {} = {}'.format(num, d, i))
