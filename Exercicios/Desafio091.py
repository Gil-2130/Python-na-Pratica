"""
Crie um programa onde 04 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número do dado
"""


# Importando biblioteca para criar números aleatórios de 1 a 6(dado)
from random import randint

# Importando biblioteca para desacelerar a execução
from time import sleep

# Importando biblioteca para obter os maiores valores do dicionário
from operator import itemgetter

# Criando um dicionário JOGO onde cada jogador terá resultados diferentes...
jogo = {'Jogador_1': randint(1, 6),
        'Jogador_2': randint(1, 6),
        'Jogador_3': randint(1, 6),
        'Jogador_4': randint(1, 6)
        }

# Variável para ranquear os jogadores
ranking = dict()

for key, value in jogo.items():
    print(f'O {key} tirou o número {value}')
    sleep(1)
# Obtendo apenas os valores do dicionário
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Imprimindo o ranking
print(ranking) # Apague esse print se achar necessário
print('-=' * 30)
print('Ranking dos jogadores!!')

# Como resultado, tivemos uma lista de tuplas. Neste caso faremos um laço para obter
# os dados de forma mais organizada
for key, value in enumerate(ranking):
    print(f'Posição {key + 1}: {value[0]} tirou {value[1]} no dado.')
    sleep(1)
