"""

Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final mostre;
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves

"""
# Criando uma lista temporária
temp = []

# Obtendo os dados da lista temporária
prin = []

# Variável para armazenar aquela que tiver o maior peso
maior_p = 0

# Variável para armazenar aquela que tiver o menor peso
menor_p = 0

# Criando laço infinito
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    # Condicional para obter o maior peso através do input
    if len(prin) == 0:
        maior_p = menor_p = temp[1]

    # Criando uma cópia do temp
    prin.append(temp[:])

    # Limpando a lista temporária(para evitar repetições)
    temp.clear()

    # Opção de interrupção do programa
    resp =  str(input('Deseja continar?'
                      '[S/N]: ')).upper().strip()[0]

    # Condicional de parada
    if resp in'Nn':
        break

print('-=' * 30)
print(f'Os dados fora {prin}')
print(f'Ao todo foram cadastrados {len(prin)} pessoas.')
