"""

Faça um programa que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra FIM, o programa se encerrará.

OBS: use cores.

"""


# Importando biblioteca para diminuir a velocidade de execução do print
from time import sleep


# Criando uma tupla de cores
cores = ('\033[m',  # 0 - Sem cores
         '\033[0;30;41m',  # 1 - Vermelho
         '\033[0;30;42m',  # 2 - Verde
         '\033[0;30;43m',  # 3 - Amarelo
         '\033[0;30;44m',  # 4 - Azul
         '\033[0;30;45m',  # 5 - Roxo
         '\033[7;30m'      # 6 - Branco
         )


# Criando função de ajuda
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[3], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)


# Função de título com cores
def titulo(msg, cor=0):
    # Obtendo o tamanho da msg
    tam = len(msg) + 4
    # Imprimindo a cor
    print(cores[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(cores[0], end='')
    sleep(1)


# Programa Principal
comando = ''

# laço para solicitar o HELP enquanto a condicional não for satisfeita
while True:
    titulo('Sistema de Ajuda PyHELP', 3)
    comando = str(input('Função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 2)
