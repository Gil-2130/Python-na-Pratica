"""
Faça um programa que leia o nome e média do aluno,
guardando também a situação em um dicionário.
No final mostre o conteúdo da estrutura na tela
"""
nome = dict()
media = dict()
situacao = list()

for c in range(0, 1):
    nome = str(input('Nome: '))
    media = float(input(f'Média de {nome}: '))
    print(f'Nome é igual a {nome}')
    print(f'Média é igual a {media}')
    if media >= 7:
        situacao.append(media)
        print(f'O aluno(a) {nome} teve média acima de 7 e está Aprovado!')
    else:
        print(f'O aluno(a) {nome} teve média abaixo de 7 e está Reprovado!')