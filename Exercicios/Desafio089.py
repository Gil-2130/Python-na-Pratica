"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.

"""

# Criando uma variavel tipo "ficha"
ficha = list()

# Criando laço infinito
while True:
    # variavel para nome
    nome = str(input('Nome: '))
    # Obtendo notas
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    # Calculando a média
    media = (nota1 + nota2) / 2
    # Adicionando os elementos á lista
    ficha.append([nome, [nota1, nota2], media])
    # Continuação ou interrupção do programa
    resp =  str(input('Deseja continuar?'
                      '[S/N]: ')).upper().strip()[0]
    if resp in 'Nn':
        break

# imprimindo resultados
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

# laço para pegarmos os itens da ficha
for indice, item in enumerate(ficha):
    print(f'{indice:<4}{item[0]:<10}{item[2]:>8.1f}')

# Laço infinito para que as notas sejam imprimidas para cada aluno
while True:
    print('-' * 35)
    opc = int(input('Para qual aluno você deseja ver as notas? (999 Encerra): '))

    # Condicional para encerramento do programa
    if opc == 999:
        break

    #
    if opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}')
# print de encerramento do programa
print('<<< VOLTE SEMPRE >>>')
