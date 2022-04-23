"""
Crie um programa que crie uma matriz 3 x 3
e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta
"""

# Criando variavel que irá armazenar as listas
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Criando um laço dentro do outro para obtermos posicionarmos os elementos na matriz
for i in range(0, 3):
    # Segundo laço para cada elemento de "i"
    for j in range(0, 3):
        # Adicionado os elementos do primeiro laço na primeira linha e assim sucessivamente.
        matriz[i][j] = int(input(f'Digite um valor para [{i},{j}]: '))

print('-=' * 30)

# Novo laço, desta vez para criar a matriz, com cada elemento dentro dela.
for l in range(0, 3):
    for m in range(0, 3):
        print(f'[{matriz[l][m]:^5}]', end='')
    print()
