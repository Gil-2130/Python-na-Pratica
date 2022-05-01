"""
Faça um programa que ajude um jogador da megasena a criar palpites.

O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre e 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.

"""
from random import randint

num_0 = randint(0, 60)

palpite = []
print(num_0)
for i in range(0, 6):
