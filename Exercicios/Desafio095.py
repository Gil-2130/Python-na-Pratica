"""
Aprimore o desafio093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

# #                           ======== CÓDIGO ORIGINAL =======
#
# # Criando dicionário para "jogadores"
# jogador = dict()
# # Lista para partidas
# partidas = list()
# # Adicionando dados ao dicionário criado anteriormente
# jogador['Nome'] = str(input('Nome do Jogador: '))
# # Total de partidas
# total = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
#
# # Criando um laço para obtermos a quantidade de gols por partida
# for c in range(0, total):
#     partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
#
# # Criando uma cópia de partidas, que agora possuirá uma listagem com os gols
# jogador['Gols'] = partidas[:]
# # Obtendo a soma total de gols já feitos pelo jogador
# jogador['Total Gols'] = sum(partidas)
#
# # Imprimindo organizador de código
# print('-=' * 30)
#
# # Imprimindo nosso dicionário
# print(jogador)
#
# # Imprimindo organizador de código
# print('-=' * 30)
#
# # laço para obter indice e valor dentro do dicionário
# for key, value in jogador.items():
#     print(f'O campo {key} tem valor {value}')
#
# # Imprimindo organizador de código
# print('-=' * 30)
#
# print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partida.s')
#
# # Criando laço apenas para enumerar cada partida e seu respecivo saldo de gols
# for indice, valor in enumerate(jogador["Gols"]):
#     print(f'    => Na partida {indice + 1}, fez {valor} gols.')
# # Print final com a soma dos gols
# print(f'Foi um total de {jogador["Total Gols"]} gols.')




#                       ========= CÓDIGO MODIFICADO =========

# Criando dicionário para adicionar o jogador
jogador = dict()
# Criando lista para adicionar jogadores
time = list()
# Lista para partidas
partidas = list()

# Criando um laço infinito
while True:

    # Toda vez que o jogador for adicionado ao time, iremos limpar o dicionário para evitar repetiçoes
    jogador.clear()
    # Adicionando dados ao dicionário criado anteriormente
    jogador['Nome'] = str(input('Nome do Jogador: '))
    # Total de partidas
    total = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    # Limpando as partidas
    partidas.clear()
    # Criando um laço para obtermos a quantidade de gols por partida
    for c in range(0, total):
        # De acordo com o número de partidas, iremos solicitar os gols por partida e adicionar a uma lista
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))

    # Criando uma cópia de partidas, que agora possuirá uma listagem com os gols
    jogador['Gols'] = partidas[:]
    # Obtendo a soma total de gols já feitos pelo jogador
    jogador['Total Gols'] = sum(partidas)

    # Agora iremos adicionar o jogador a uma lista
    time.append(jogador.copy())

    # Condicional para continuar ou interromper o loop
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        # Condicional apenas para receber a opção correta
        if resp in 'SN':
            break
        else:
            print('ERRO! Digite S para Sim ou N para Não.')
    # Interrompendo o programa
    if resp == 'N':
        break

# Imprimindo organizador de código
print('-=' * 30)
print('COD ', end='')

# laço para pegar as chaves do dicionário
for key in jogador.keys():
    print(f'{key:<15}', end='')

print()
print('-' * 40)

# Laço para pegar indice e valor do time
for indice, chave in enumerate(time):
    print(f'{indice + 1:>4} ', end='')
    for valor in chave.values():
        print(f'{str(valor):<15}', end='')
    print()
print('-' * 40)

# Opcional para mostrar os dados de cada jogador separadamente (Análise de Dados)
while True:
    busca = int(input('Mostrar dados de qual jogador? 999 encerra a busca: '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'ERRO! Não Existe Jogador com código {busca}!')
    else:
        print(f' -- DADOS DO JOGADOR {time[busca - 1]["Nome"]}: ')
        for partida, gol in enumerate(time[busca - 1]['Gols']):
            print(f'    No jogo {partida + 1}, {time[busca - 1]["Nome"]} fez {gol} gols.')

    print('-' * 40)

print('FIM DO PROGRAMA.')