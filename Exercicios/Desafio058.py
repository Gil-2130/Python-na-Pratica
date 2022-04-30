"""

Melhore o jogo do DESAFIO28 onde o computador vai pensar em um numero entre 0 e 10

Porém, o player tentara acertar, mostrando no final, quantos palpites foram necessários para acertar

"""

# Importando módulo para criar numeros aleatórios
from random import randint

#  palpite do PC
pc = randint(0, 10)

# Imprimindo msg simulando o PC
print('(PC)-> Pensei em um número entre 0 e 10.\n'
      'Você consegue adivinhar?...')

# Inicializando variavel que armazenará valor booleano falso enquanto o player não acertar
acertou = False

# Variavel que armazenará a quantidade de palpites do usuário
palpite = 0

# enquanto a variavel não for verdadeira
while not acertou:

    # input do player
    jogador = int(input('Qual é o seu palpite? '))

    # Contagem do número de palpites
    palpite = palpite + 1

    # Condicional quando palpite e numero forem iguais
    if jogador < pc:
        print('Palpite baixo!!')

    elif jogador > pc:
        print('Palpite Alto')

    elif jogador == pc:
        acertou = True
        print('Acertou, Parabéns')
        print('Você deu {} palpites'.format(palpite))
    else:
        print('Palpite inválido')
print('-=-' *10)
print('Fim do Programa')
