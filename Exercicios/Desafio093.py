"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois irá ler a quantidade de gols feitos em cada parida.
No final, tudo iso será guardado num dicionário, incluindo o total de gols feitos
durante o campeonato.
"""

# Criando dicionário para jogador
jogador = dict()
# Criando uma lista para armazenar as partidas
partidas = list()
# Adicionando elementos ao dicionário
jogador['Nome'] = str(input('Nome do jogador: '))
# Quantidade de partidas do jogador
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))

# laço para obter a quantidade de gols por partida
for c in range(0, tot):
    # Adicionando os gols á lista
    partidas.append(int(input(f'Quantos gols {jogador["Nome"]} marcou na partida {c + 1}? ')))
# Criando gols
jogador['Gols'] = partidas[:]
# Total de gols
jogador['Total'] = sum(partidas)
# Imprimindo nosso separador
print('-=' * 30)
# Imprimindo nosso dicionário
print(jogador)
# Imprimindo nosso separador
print('-=' * 30)

# Laço para obter item e valor do dicionário
for key, value in jogador.items():
    print(f'O campo {key} tem valor {value}')
# Imprimindo nosso separador
print('-=' * 30)
# Imprimindo a quantidade de partidas jogadas
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
# Laço
for i, v in enumerate(jogador['Gols']):
    print(f'    => Na partida {i + 1}, {jogador["Nome"]} fez {v} gols.')
print(f'No total, {jogador["Nome"]} fez {jogador["Total"]} gols.')

