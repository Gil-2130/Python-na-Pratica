"""
Aprimore o desafio anterior(desafio086), mostrando no final;

A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

# Criando Matriz (listas dentro de uma lista)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Variável para soma dos valores pares
soma_par = 0
# Variável para soma dos valores da terceira coluna
soma_col = 0
# Variavel para obter o maior valor
maior_v = 0

# Criando um laço "linha"
for linha in range(0, 3):
    # Criando outro laço "j" para cada elemento de "i"
    for coluna in range(0, 3):
        # Adicionado os elementos do primeiro e segundo laço á matriz
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))

        # Obtendo os valores pares
        if matriz[linha][coluna] % 2 == 0:
            soma_par = soma_par + matriz[linha][coluna]

# Imprimindo um organizador de código
print('-=' * 30)

# Criando laço, desta vez para imprimir a matriz em formato 3x3
for linha in range(0,3):
    for coluna in range(0 ,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print('-=' * 30)
# Imprimindo a soma dos valores pares
print(f'A soma dos valores pares foi: {soma_par}.')

# Criando laço para calcular os valores da terceira coluna
for linha in range(0,3):
    soma_col = soma_col + matriz[linha][2]
# Imprimindo a soma dos valores na terceira coluna
print(f'A soma da terceira coluna é: {soma_col}')


# Criando laço para obter o maior valor da segunda linha
for coluna in range(0, 3):
    # Condicional para obter o maior valor começando na primeira coluna e em seguida na segunda linha
    if coluna == 0:
        # Então a variável receberá o maior valor da segunda linha começando na primeira coluna
        maior_v = matriz[1][coluna]
    # caso contrário (a lógica é a mesma para todas as colunas, mas a linha será sempre a mesma
    elif matriz[1][coluna] > maior_v:
        maior_v = matriz[1][coluna]

# Imprimindo o resultado
print(f'O maior valor encontrado na segunda linha foi {maior_v}')
