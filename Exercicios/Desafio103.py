'''

Faça um programa que contenha uma função chamada ficha(),
que receba dois parãmtros opcionais:
O nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha o jogador,
mesmo que algum dado não tenha sido informado corretamente.

'''


# Criando função
def ficha(jogador='<Desconhecido>', gol=0):
    print(f'O jogador {jogador.upper()} fez {gol} gols na partida.')


# Programa principal
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))

# Condicional para verificar se gols é um valor numérico
if gols.isnumeric():
    # Se sim, converteremos para inteiro
    gols = int(gols)
# Caso contrário, o valor 0 será atribuído a essa variável.
else:
    gols = 0
# Se o nome do jogador receber um valor vazio
if nome.strip() == '':
    ficha(gol=gols)
# Caso Contrário
else:
    # Recebebendo nome e gols
    ficha(nome, gols)
