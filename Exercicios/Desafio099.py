"""
Faça um programa que tenha a função chamada maior(),
esta receberá vários parâmetros com valores inteiros.
Nosso programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
# Importando biblioteca para dar sleep
from time import sleep


# Criando a função solicitada
def maior(* num):
    # Criando contador
    cont = 0

    # Variável que receberá o maior valor
    maior = 0
    print('-' * 35)
    print('Analisando os valores informados...')

    # Imprimindo resultados através de um laço
    for valor in num:
        # Imprimindo o valor do laço com um atraso
        print(f'{valor} ', end='', flush=True)
        sleep(0.4)

        # Condicional para obter o maior valor
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        # Contando os elementos adicionados
        cont = cont + 1
    print(f'Foram informados {cont} valores no total.')
    print(f'O maior valor informado foi {maior}.')

# Programa Principal
maior(2, 9, 4, 5, 6)
maior(4, 7, 8)
maior(10,15, 20)
