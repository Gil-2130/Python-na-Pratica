"""

Crie uma tupla preenchida com os 20 primeiros colocados da tabela
do campeonato brasileiro de Futebol, na ordem de colocação.
DEpois mostre:
A). Apenas os 5 primeiros colocados.
B). Os últimos 04 colocados da tabela.
C). Uma lista com os times em ordem alfabética.
D). Em que posição está o time da chapecoense.

"""

# Tupla com os times
times = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 
         'Botafogo', 'Ceará-SC', 'Corinthians', 'Chapecoense', 'Cuiabá',
         'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional', 
         'Juventude', 'Palmeiras', 'Santos', 'Bragantino', 'São Paulo')

# laço para obter os 5 primeiros colocados
print('Os 5 primeiros colocados são: ')
for i in times[0:5]:
    print(i)
# Imprimindo espaçadores (organização do código)
print('=-='*20)

# laço para imprimir os 04 ultimos colocados
print('Os 4 ultimos colocados são:')
for i in times[-4:]:
    print(i)

# imprimindo espaçadores(organização do código
print('=-='*20)

# Imprimindo a tupla em ordem alfabética
print('Imprimindo a tupla em ordem alfabética:')
for i in sorted(times):
    print(i)

print('=-='*20)

# Imprimindo um time da tupla
print('Imprimindo o time do Chapecoense: ')
for i, pos in enumerate(times):
    if 'Chapecoense' in pos:
        # identificando a posição do time
        print(f'O time {pos}, encontra-se na {i + 1}ª posição.')



# Resposta do professor
# Tupla com os times
times = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí',
         'Botafogo', 'Ceará-SC', 'Corinthians', 'Chapecoense', 'Cuiabá',
         'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional',
         'Juventude', 'Palmeiras', 'Santos', 'Bragantino', 'São Paulo')

print('-=' * 15)
print(f'Lista de Times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros colocados são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimos colocados são {times[-4:]}')
print('-=' * 15)
print('Os times em ordem alfabética:\n',
      sorted(times))
print('-=' * 15)
print(f'O time do chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
