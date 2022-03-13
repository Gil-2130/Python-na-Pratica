"""
Crie um programa que leia vários números inteiros pelo teclado.

No Final da execução, mostre a média entre todos os valores e qual foi o MAIOR e MENOR
valores lidos.

O programa deve Perguntar ao usuario se ele quer ou não continuar a digitar valores.
"""

# Variavel para armazenar respostas (s/n) do usuário
resp = 'S'

# Vaiavel para armazenar a soma dos valoers para cálculo posterior da média
soma = 0

# Variável para armazenar as médias
media = 0

# Variavel contadora de inputs recebidos
quant = 0

maior = 0
menor = 0

# Enquanto a resposta for SIM
while resp in 'Ss':

    # Solicitando um número para o usuário
    num = int(input('Digite um número: '))

    # acumulador
    soma = soma + num

    # Contador da quantidade números recebidos (para calcular a média)
    quant = quant + 1

    # Solicitando ao usuário, se o mesmo deseja continuar
    resp = str(input('Deseja Continuar?\n'
                     '[S/N] ->  ')).upper().strip()[0]

    # Verificando maior e menor valor
    if quant == 1:
        maior = menor = num

    else:
        if num > maior:
            maior = num
        elif num < maior:
            menor = num

# Calculando a média
media = soma / quant

# Imprimindo o resultado
print('Você digitou {} números. A soma total foi {}\n'
      'A média do total foi de {}\n'
      'O maior valor e menor valor são respectivamente {} e {}'.format(quant, soma, media, menor, maior))

# Fim
print('Fim do Programa!')
