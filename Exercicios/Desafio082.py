"""
Crie um programa que vai ler vários números e colocar em uma lista.
DEpois disso, crie duas listas extras que vão conter apenas os
valores pares e os ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas
"""

# Criando lista vazia
numeros = list()
# Lista de numeros pares
par = list()
# Lista de numeros ímpares
impar = list()

# Laço infinito para obter os numeros
while True:
    # Obtendo os inputs dos usuários
    n = int(input('Digite um número:'))
    numeros.append(n)

    # Opção para continuar ou encerrar o programa
    r = str(input('Deseja continuar?\n'
                  '[Sim/Não]: ')).upper().strip()[0]
    # Condicional para encerramento do programa
    if r in 'Nn':
        break
    # Obtendo os numeros pares e guardando dentro de uma variável
    if n % 2 == 0:
        par.append(n)
        
    # Obtendo os números ímpares e guardando dentro de uma variável
    else:
        impar.append(n)

# Imprimindo a lista completa
print(f'A lista possui os números: {numeros}')
# imprimindo números pares
print(f'Os números pares são: {par}')
# Imprimindo os números ímpares
print(f'Os números ímpares são: {impar}')
