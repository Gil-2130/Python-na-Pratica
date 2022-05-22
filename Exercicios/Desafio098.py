"""
Faça um programa que tenha a função chamada contador(),
que receberá 03 parâmetros; INÍCIO, FIM e PASSO e realize a contagem.

Seu programa tem que realizar 03 contagens através da função criada:
A) De 1 até 10, a cada 1
B) DE 10 até 0, a cada 2
C) Uma contagem personalizada
"""

# Importando biblioteca apenas para diminuir o tempo de execução do print
from time import sleep


# Criando função contador (inicio, fim e passo)
def contador(i, f, p):
    # caso o passo for negativo(menor que 0) passo será negativo
    if p < 0:
        p = p * -1
    # Caso o passo for igual a 0, passo será 1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f}, indo de {p} em {p}')

    # Criando contador
    cont = i
    # Condicional caso o início for menor que o fim
    if i < f:
        # Criando laço enquanto o contador for menor que o fim e somando ao passo
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            # Chamando a função de sleep
            sleep(0.5)
            # somando o contador ao passo
            cont = cont + p
        print('FIM!')

    # caso contrário
    else:
        # Criando novo contador
        cont = i
        # Criando laço enquanto o contador for maior ou igual ao fim
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            # Chamando a função de sleep
            sleep(0.5)
            # Agora o contador será subtraído pelo valor de p
            cont = cont - p
        print('FIM!')


# Programa principal (Início, meio e fim)
contador(1, 10, 1)
contador(10, 0, 2)
# Programa para o usuário
print('Contagem personalizada(usuário): ')
ini = int(input('Digite o Início da Contagem: '))
fim = int(input('Digite o FIm da Contagem: '))
pas = int(input('Agora digite o passo da contagem: '))
# chamando a função com os parâmetros especificados pelo usuário
contador(ini, fim, pas)
