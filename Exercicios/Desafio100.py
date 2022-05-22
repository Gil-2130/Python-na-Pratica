"""
Faça um programa que tenha uma LISTA chamada NUMEROS[] e duas funções
chamadas SORTEIA() e SOMAPAR().
A primeira função vai sortear 5 números e colocá-los dentro da lista
e a segunda função vai mostrar a SOMA entre todos os valores PARES
sorteados pela função anterior.
"""

# Importando biblioteca para trabalhar com números randomizados
from random import randint
# Desacelerando a execução do print
from time import sleep


# Criando função que sorteará números
def sorteia(lista):
    print('Números Sorteados: ')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.4)
    print('\nFINALIZADO.')


# Criando função que soma apenas valores pares
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)
