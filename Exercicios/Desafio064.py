"""
Crie um programa que leia vários número sinteiros pelo teclado.

O programa só irá parar quando o usuário digitar o valor 999, que é a condição de parada.

No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag)
"""
# Variável para armazenar os valores
num = 0
cont = 0
soma = 0

num = int(input('Digite um número [999 para encerrar]: '))
while num != 999:

    soma = soma + num
    cont = cont + 1
    num = int(input('Digite um número [999 para encerrar]: '))

print('Você digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))

print('Acabou')
