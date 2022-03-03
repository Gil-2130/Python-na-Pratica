"""
Crie um programa que faça o computador jogar jokenpô com você.
"""
print('{:=^40}'.format(' JOKENPO '))

print('=' * 40)
print('Pedra, Papel ou tesoura?\n'
      '[1] - PEDRA\n'
      '[2] - PAPEL\n'
      '[3] - TESOURA')

# Capturando o input do usuario
opcao = int(input('Qual a sua opção? '))

# trabalhando com um range de números
from random import randint

# Fazendo o PC escolher uma opção (O intuito é ganhar dele)
pc = randint(1, 3)

# Condicional de EMPATE
if opcao == pc:
    print('PC e Usuário escolheram a mesma coisa!'.format(pc, opcao))
    print('EMPATE!!!')

# Condiconal PEDRA e TESOURA
elif opcao == 1 and pc == 3:
    print('O PC escolheu TESOURA e o usuário escolheu PEDRA')
    print('O Usuário VENCEU!!!')

# Condicional PEDRA e PAPEL
elif opcao == 1 and pc == 2:
    print('O PC escolheu PAPEL e o usuario escolheu PEDRA')
    print('O PC VENCEU!!!')

# Condicional PAPEL  e tesoura
elif opcao == 2 and pc == 3:
    print('O PC escolheu TESOURA e o usuario escolheu PAPEL')
    print('O PC VENCEU!!!')

# Condicional PAPEL e PEDRA
elif opcao == 2 and pc == 1:
    print('O PC escolheu PEDRA e o usuario escolheu PAPEL')
    print('O USUARIO VENCEU!!!')

# Condicional TESOURA E PAPEL
elif opcao == 3 and pc == 2:
    print('O PC escolheu PAPEL e o usuário escolheu TESOURA')
    print('O USUARIO VENCEU!!!')

# Condicional TESOURA e PEDRA
elif opcao == 3 and pc == 1:
    print('O PC escolheu PEDRA e o usuario escolheu TESOURA')
    print('O PC VENCEU!!!')

# Tratando erros
else:
    opcao = 0
    print('Opção inválida!!!')
print('-=-' * 15)




# Resolução do professor

# Importando módulo para escolher randomicamente um número
from random import randint

# Importando módulo para sleep
from time import sleep

# colocando as opões em uma tupla
itens = ('PEDRA', 'PAPEL', 'TESOURA')

# opçoes do PC
pc = randint(1, 3)

# imprimindo as opções para o usuario
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

# Solicitando ao usuário que digite uma opção
player = int(input('Sua opção: '))

# Imprimindo JOKENPO
print('JO...', end='')
sleep(0.8)
print('KEN...', end='')
sleep(0.8)
print('PO!!')


# Imprimindo um separador para organização do código
print('-=-' * 15)

# Imprimindo a opção do PC
print('PC escolheu {}'.format(itens[pc]))

# Imprimindo a opção do player
print('PLAYER escolheu {}'.format(itens[player]))

# Adicionando novo separador
print('-=-' * 15)

# Condição aninhada ao PC escolher 1 (PEDRA)
if pc == 1:
    if player == 1:
        print('EMPATE!!!')
    elif player == 2:
        print('PLAYER VENCEU!!!')
    elif player == 3:
        print('PC VENCEU!!!')
    else:
        player = 0
        print('Opção inválida!!!')

# Condição aninhada ao PC escolher 2 (PAPEL)
elif pc == 2:
    if player == 1:
        print('PC VENCEU!!!')
    elif player == 2:
        print('EMPATE!!!')
    elif player == 3:
        print('PLAYER VENCEU!!!')
    else:
        player = 0
        print('Opção invãlida!!!')

# Condição aninhada ao PC escolher 3 (TESOURA)
elif pc == 3:
    if player == 1:
        print('PLAYER VENCEU!!!')
    elif player == 2:
        print('PC VENCEU!!!')
    elif player == 3:
        print('EMPATE!!!')
    else:
        player = 0
        print('Opção Inválida!!!')

