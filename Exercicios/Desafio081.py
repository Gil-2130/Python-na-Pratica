"""

Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso mostre;
A). Quantos números foram digitados?
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
print(f'Ordenando a lista em ordem decrescente: {numeros}')

# Verificando se o número 5 está ou não na lista
for i in numeros:

    # Condicional para verificar se o 5 está na lista, ou seja;
    # Se algum valor dividido por 1 for igual a 5,
    # Então este valor é 5, certo?
    if i * 1 == 5:

        # Imprimindo o número 5 e a sua posição
        print(f'O numero 5 foi encontrado e está no indice {numeros.index(5)}')
        # # Imprimindo o indice do 5
        # print(f'{numeros.index(5)}...')

    # Se então, o número não estiver na lista, imprima a msg abaixo.
    else:
        print('O número 5 não encontrado...')

print('Fim do programa')



# SOLUÇÃO DO PROFESSOR

# Criando uma lista vazia
valores = list()

# Criando um laço infinito
while True:
    # Adicionado os valores do input à lista
    valores.append(int(input('Digite qualquer valor: ')))
    # Adicionando opção para encerramento do programa
    resp = str(input('Deseja continuar?\n'
                     '[S/N]')).upper().strip()[0]
    # Condicional para encerrar ou continuar o programa
    if resp in 'Nn':
        break
# Imprimindo separador(para separar as linhas
print('-=' * 30)
# Imprimindo a lista e a quantidade de elementos que ela possui
print(f'A lista {valores} contém {len(valores)} elementos')
# Imprimindo a lista em ordem decrescente
print(f'A lista em ordem Decrescente é: {valores.sort(reverse=True)}')
# Verificando se o número está na lista
if 5 in valores:
    print('O valor 5 faz parte da lista!')
# Caso contrário
else:
    print('O valor 5 não foi encontrado na lista!')
