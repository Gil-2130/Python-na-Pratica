"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso mostre;
A). Quantos números foram digitados.
B). A lista de valores, ordenada de forma decrescente
C). Se o valor 5 foi digitado e está na lista sim ou não
"""
# Criando uma lista vazia
numeros = list()

# Criando um laço infinito
while True:
    # Criando uma variavel para receber os inputs
    n = int(input('Digite um número: '))

    # Adicionado os inputs à lista
    numeros.append(n)

    # Variavel que recebe o input de fluxo(cont. ou encerra) do programa
    r = str(input('Deseja Continuar?\n'
                  '[Sim/Não]: ')).upper().strip()[0]

    # Condicional para continuação ou interrupção do programa
    if r in 'Nn':
        break

# Imprimindo a lista
print(f'Foram digitados os números => {numeros}')

# Imprimindo a lista ordenada em forma decrescente
numeros.sort(reverse=True)
print(f'Ordenando a lista => {numeros}')

# Imprimindo o número 5 e sua posição
print(f'O numero 5 está na lista, na posição ', end='')

# Verificando se o número 5 está ou não na lista
for i in numeros:
    
    # Condicional para verificar se o 5 está na lista, ou seja;
    # Se algum valor dividido por 1 for igual a 5,
    # Então este valor é 5, certo?
    if i % 1 == 5:
        # Imprimindo o indice do 5
        print(f'{numeros.index(5)}...', end='')
        
print()
print('O número 5 não se encontra nesta lista.')
