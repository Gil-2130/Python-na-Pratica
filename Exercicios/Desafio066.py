"""

Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuario digitar 999, que é a condição
de parada.

No final mostre quantos numeros foram digitados e qual foi a soma entre eles(Desconsiderando a flag)

"""

# Incializando variável para armazenar os inputs
n = 0

# Variavel de soma dos valores
soma = 0

# Variavel Contabilizadora dos valores
cont = 0
print('=-='*10)

# Enquanto...
while True:
    # Solicitando um número ao usuário
    n = int(input('Digite um número: '))
    # Condição de interrupção do WHILE
    if n == 999:
        print('=-=' * 10)
        print('Interrompendo o programa -> Imprimindo Resultados!')
        break
    # Contabilizando quantos valores foram digitados
    cont = cont + 1
    # Somando todos os valores digitados
    soma = soma + n

# Imprimindo Resultados
print('=-='*10)
print(f'Foram digitados {cont} números\n'
      f'A soma de todos os valores foi {soma}')
