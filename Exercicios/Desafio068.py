# Crie um programa que jogue par ou impar com o PC.
#
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Biblioteca para recolher números aleatórios
from random import randint

# Jogador PC
pc = randint(1,10)

# variavel para armazenar o input
num = 0

# Contador da quantidade de vitórias(Faça de perdas também se assim desejar)
ganha = 0

# Enquanto...
while True:
    # Separador de linhas
    print('==' * 20)
    # Solicitando um número para o usuário
    num = int(input('Digite um número: '))
    # Solitando que escolha PAR ou ÍMPAR
    opcao = str(input('você quer par ou ímpar?\n'
                    '[P/I]: ')).upper().strip()[0]
    print('=='* 20)

    # Condicional se o player jogar um número PAR e desejar PAR
    if num % 2 == 0 and opcao in 'Pp':

        # Se o PC escolher ÍMPAR e digitar um número par
        if pc % 2 == 0:
            # Contador de vitórias do usuário
            ganha = ganha + 1
            print(f'O PC pediu ÍMPAR e jogou {pc}\n'
                  f'O Usuário pediu PAR e jogou {num}\n'
                  f'O usuário VENCEU!! ')

        # Se o PC escolher ÍMPAR e digitar um número ímpar
        elif pc % 2 == 1:
            print(f'O PC pediu ÍMPAR e jogou {pc}\n'
                  f'O Usuário pediu PAR e jogou {num}\n'
                  f'O PC VENCEU!! ')
            print('FIM do jogo!')
            # Interrompendo o jogo se o usuário Perder
            break

    # Condicional se o player jogar um número IMPAR e desejar PAR
    elif num % 2 == 1 and opcao in 'Pp':

        # Se o PC escolher PAR e quer ÍMPAR
        if pc % 2 == 0:
            print(f'O PC pediu ÍMPAR e jogou {pc}\n'
                  f'O Usuário pediu PAR e jogou {num}\n'
                  f'O PC VENCEU!! ')
            print('FIM do jogo!')
            # Interrompendo o jogo se o usuário perder
            break

        # Se o PC escoher ÍMPAR e quer ÍMPAR
        elif pc % 2 == 1:
            # Contador de vitórias
            ganha = ganha + 1
            print(f'O PC pediu PAR e jogou {pc}\n'
                  f'O Usuário pediu ÍMPAR e jogou {num}\n'
                  f'O Usuário VENCEU!! ')


    # Condicional se o player jogar PAR e quer ÍMPAR
    elif num % 2 == 0 and opcao in 'Ii':

        # Se o PC colocar PAR e quer PAR
        if pc % 2 == 0:
            print(f'O PC pediu PAR e jogou {pc}\n'
                  f'O Usuário pediu ÍMPAR e jogou {num}\n'
                  f'O PC VENCEU!! ')
            print('FIM do jogo!')
            # Interrompendo o jogo se o usuário perder.
            break

        # Se o PC colocar ÍMPAR e quer PAR
        elif pc % 2 == 1:
            # Contador de vitórias
            ganha = ganha + 1
            print(f'O PC pediu PAR e jogou {pc}\n'
                  f'O Usuário pediu ÍMPAR e jogou {num}\n'
                  f'O usuário VENCEU!! ')

    # Condicional se o player jogar ÍMPAR e quer ÍMPAR
    elif num % 2 == 1 and opcao in 'Ii':

        # Se o PC colocar PAR e quer PAR
        if pc % 2 == 0:
            # Contador de vitórias
            ganha = ganha + 1
            print(f'O PC pediu PAR e jogou {pc}\n'
                  f'O Usuário pediu ÍMPAR e jogou {num}\n'
                  f'O usuário VENCEU!! ')

        # Se o PC colocar ÍMPAR e quer PAR
        elif pc % 2 == 1:
            print(f'O PC pediu PAR e jogou {pc}\n'
                  f'O Usuário pediu ÍMPAR e jogou {num}\n'
                  f'O PC VENCEU!! ')
            print('FIM do jogo!')
            # Interrompendo o game se o usuário Perder
            break

# Mensagem de fim do programa
print('==' * 20)
print(f'O Usuário ganhou {ganha} vezes!' if ganha > 0 else 'O usuário perdeu a rodada!')

