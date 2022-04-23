"""
Crie um programa onde o usuário possa digitar 07 valores
numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.

"""
# Criando lista que adicionará os valores do input
valor = list()
# Lista para armazenar os valores pares
par = list()
# Lista para armazenar os valores ímpares
impar = list()

# Laço infinito
for i in range(0, 8):
    # Obtendo o input do usuário
    v = int(input('Digite um valor: '))
    # Adicionando o input para outra variável
    valor.append(v)

    # Condicional para obter os valores pares
    if v % 2 == 0:
        # Adicionado os valores pares
        par.append(v)
    # Caso contrário, os valores serão ímpares
    else:
        # Adicionando os valores ímpares para a variável correspondente
        impar.append(v)

# Imprimindo resultados

# Imprimindo a lista completa
print(f'Os valores digitados foram {valor}')
# Imprimindo a lista de pares ordenada
print(f'Os valores pares da lista são {sorted(par)}.')
# Imprimindo a lista de ímpares ordenada
print(f'Os valores ímpares da lista são {sorted(impar)}.')



# ======= RESOLUÇÃO DO PROFESSOR =====

# Criando listas dentro de listas
num = [[], []]

# Variavel para armazenar os valores do input
valor = 0
# Criando um laço
for c in range(1, 8):
    # Obtendo os valores
    valor = int(input(f'Digite o {c}° valor: '))

    # Condicional para valores pares
    if valor % 2 == 0:
        num[0].append(valor)
    # Caso contrário, valores serão ímpares
    else:
        num[1].append(valor)

# Ordenando as listas
num[0].sort()
num[1].sort()

print('-=' * 30)
print(f'Os valores pares são {sorted(num[0])}')
print(f'Os valores ímpares encontrados foram: {sorted(num[1])}')
