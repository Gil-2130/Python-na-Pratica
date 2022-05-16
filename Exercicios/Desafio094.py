"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em dicionários e todos os dicionários em
uma lista.
No final mostre:
A)- Quantas pessoas foram cadastradas
B)- A média de idade do grupo.
C)- Uma lista com todas as mulheres
D)- Uma lista com todas as pessoas com idade acima da média.
"""

# Criando um dicionário para guardar "pessoas"
pessoas = dict()

# Criando lista para guardar várias pessoas
galera = list()

# Obtendo a soma das idades
idade = []

# Criando um laço para obter os dados e condicionais
while True:
    # Precisamos sempre esvaziar o dicionário antes de adicionar pessoas
    pessoas.clear()

    # Adicionando elementos ao dicionário criado
    # Nome
    pessoas['Nome'] = str(input('Nome: '))
    # Sexo, com validação do input dos dados
    while True:
        pessoas['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoas['Sexo'] in 'MF':
            break
        else:
            print('ERRO!! Por favor digite M para Masc. ou F para Fem.!')

    # Idade
    pessoas['Idade'] = int(input('Idade: '))
    idade.append(pessoas['Idade'])
    # Criando uma cópia de "pessoas"
    galera.append(pessoas.copy())

    # Laço infinito para continuação do programa
    while True:
        # Condicional para continuação da execução do programa
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Por favor Digite S para continuar ou N para interromper.')
    # Interrompendo o 1° laço infinito
    if resp == 'N':
        break

# Organizador
print('-=' * 30)

# Imprimindo quantas pessoas foram cadastradas
print(f'Temos {len(galera)} pessoas cadastradas.')

# Imprimindo a média de idade do grupo
print(f'A média de idade do grupo é {sum(idade) / len(galera):.2f} anos.')

# Obtendo os nomes das mulheres da lista
print('As mulheres cadastradas foram: ')
for pessoa in galera:
    if pessoa['Sexo'] in 'Ff':
        print(f'    {pessoa["Nome"]} ')

# Obtendo a lista das pessoas com idade acima de média
print('As pessoas com idade acima da média são: ')
for pessoa in galera:
    if pessoa['Idade'] >= sum(idade) / len(galera):
        print('     ', end='')
        for key, value in pessoa.items():
            print(f'{key} = {value}; ', end='')
        print()

print('FIM do Programa!!')
