"""
Faça um programa que leia 05 valores numéricos e guarde em uma lista.

No final mostre; Qual foi o menor e maior valor digitado e as suas respectivas
posições na lista

"""
# Minha Solução

# Criando uma lista vazia
valores = []

# laço para solicitar um range de inputs
for i in range(1):
    # Adicionando os inputs à lista vazia
    valores.append(int(input('Digite um valor na posição 0: ')))
    valores.append(int(input('Digite um valor na posição 1: ')))
    valores.append(int(input('Digite um valor na posição 2: ')))
    valores.append(int(input('Digite um valor na posição 3: ')))
    valores.append(int(input('Digite um valor na posição 4: ')))
# Imprimindo a lista
print(f'Os valores digitados foram: {valores}')

# Encontrando o maior valor e em qual indice ele se encontra
print(f'O maior valor encontrado foi {max(valores)},\n',
      f'O valor está no indice {valores.index(max(valores))}')

# Encontrando o menor valor e em qual indice ele está
print(f'O menor valor encontrado foi {min(valores)},\n',
      f'O valor está no indice {valores.index(min(valores))}')




""" Resposta do Professor """
# Criando uma lista vazia
listanum = []

# Criando variável para armazenar o maior valor da lista
maior = 0

# Criando variavel para armazenar o menor valor da lista
menor = 0

# Criando um contador para adicionar os elementos á lista
for cont in range(0, 5):

    # Adicionando os elementos á lista
    listanum.append(int(input(f'Digite um valor para a posição {cont}: ')))

    # condicional para obter o maior valor, ou seja;
    # o primeiro número será automaticamente o maior e menor valor correto?
    if cont == 0:
        maior = listanum[cont]
        menor = listanum[cont]

    # Caso contrário
    else:
        # Se o próximo número digitado for maior que o primeiro então...
        # este passará a ser o maior valor.
        if listanum[cont] > maior:
            maior = listanum[cont]

        # Se o próximo valor digitado for menor que o primeiro então...
        # este passará a ser o menor valor.
        elif listanum[cont] < menor:
            menor = listanum[cont]

# Separador (mantendo a legibilidade do código
print('=-' * 30)

# Imprimindo a lista com todos os elementos até agora
print(f'Você digitou os valores {listanum}')

# imprima a sua posição na lista(indice), para o maior valor
print(f'O maior valor digitado foi {maior} na posição ', end='')

# Laço para obter os indices do maior valor
for indice, valor in enumerate(listanum):
    # se o valor de enumerate for igual ao maior valor da lista
    if valor == maior:
        # Imprima o indice do maior valor
        print(f'{indice}... ', end='')
# Linha vazia
print()
# Imprima sua posiução na lista para o menor valor
print(f'O menor valor digitado foi {menor} na posição ', end='')

# Laço para obter os indices do menor valor
for indice, valor in enumerate(listanum):
    # Se o valor de enumerate for igual a menor valor
    if valor == menor:
        # Imprima o indice do menor valor
        print(f'{indice}... ', end='')
print()

