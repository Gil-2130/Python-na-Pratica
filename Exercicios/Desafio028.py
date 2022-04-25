"""
Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5
e peça para o usuario tentar descobrir qual foi o numero escolhido
pelo computador.

O programa deverá escrever na tela se o usuario venceu ou perdeu
"""

# Importando biliotecas
from random import randint
from time import sleep

# escolhendo um valor aleatório entre 0 e 5
rand = randint(0, 5)
# Imprimindo organizador de código
print('-==-' * 20)
print('Pensei em um número...')
print('-==-' * 20)

# Variavel que pede um número para o usuário
choose = int(input('Me diga em qual numero eu pensei: '))
print('PROCESSANDO')
sleep(1.5)

if choose == rand:
    print('Parabéns!! Você acertou')
else:
    print('Você errou!! O numero que pensei foi {}'.format(rand))
