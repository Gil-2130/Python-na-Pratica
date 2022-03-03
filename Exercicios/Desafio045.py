"""
Crie um programa que faça o computador jogar jokenpô com você.
"""

# minha solução
print('{:=^40}'.format(' JOKENPÔ '))

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
