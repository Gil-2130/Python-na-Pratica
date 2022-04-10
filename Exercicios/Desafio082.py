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

# Laço infinito para obter os números
while True:
    # Obtendo os inputs dos usuários
    n = int(input('Digite um número => '))
    numeros.append(n)

    # Opção para continuar ou encerrar o programa
    r = str(input('Deseja continuar?\n'
                  '[Sim/Não]: ')).upper().strip()[0]

    # Obtendo os números pares e guardando dentro de uma variável
    if n % 2 == 0:
        par.append(n)

    # Obtendo os números ímpares e guardando dentro de uma variável
    else:
        impar.append(n)

    # Condicional para encerramento do programa
    if r in 'Nn':
        break

# Imprimindo um separador(legibilidade do print)
print('-=' * 30)
# Imprimindo a lista completa
print(f'A lista possui os números: {numeros}')
# imprimindo números pares
print(f'Os números pares são: {par}')
# Imprimindo os números ímpares
print(f'Os números ímpares são: {impar}')

##############################################################################################################

# RESPOSTA DO PROFESSOR

# Criando uma lista vazia
num = list()

# Criando lista que guardará os valores pares
par = list()

# Criando lista que guardará os valores ímpares
impar = list()

# Criando um laço infinito
while True:
    # Obtendo o input e adicionadno á lista
    num.append(int(input('Insira qualquer valor => ')))
    # Criando variável de opção de encerramento do programa
    resp = str(input('Deseja continuar com a execução do programa?\n'
                     '[S/N] => ')).upper().strip()[0]

    # Condicional para encerramento do programa
    if resp in 'Nn':
        break

# Criando um laço para percorrer a lista e verificar números ímpares e pares
for indice, valor in enumerate(num):
    # Buscando valores pares
    if valor % 2 == 0:
        # Adicionando os valores pares á variavel
        par.append(valor)
    # Buscando os valores ímpares
    elif valor % 2 == 1:
        # Adicionando os valores ímpares
        impar.append(valor)

# Imprimindo um print espaçador
print('-=' * 30)
# Imprimindo a lista
print(f'A lista contém os elementos: {num}')
# Imprimindo os valores pares
print(f'Os valores pares são: {par}')
# Imprimindo os valores [impares
print(f'Os valores ímpares são: {impar}')
