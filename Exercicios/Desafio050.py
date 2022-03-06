"""
desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for impar, desconsidere-o
"""

# Variavel que armazenará os valores
soma = 0

# laço de repetição do input
for i in range(0, 6):

    # Input dos dados
    n = int(input('Digite um número: '))

    # Condicional para guardar apenas números pares
    if n % 2 == 0:

        # adicionado o resultado do input à variavel
        soma = soma + n
        #print('')      não imprima nada, apenas faça a adição dos números pares

    else:
        print('NÚMEROS ÍMPARES NÃO SÂO PERMITIDOS!!')

# Imprimindo os resultados
print(soma)
