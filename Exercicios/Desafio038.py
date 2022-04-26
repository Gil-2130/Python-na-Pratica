"""
Escreva um programa que leia dois numeros inteiros
e compare-os, mostrando na tela uma mensagem;

O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais
"""

# Obtendo um valor para o usuário
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

# Condicional de comparação
if n1 > n2:
    print('O primeiro número ({}), é maior que {} .'.format(n1, n2))
elif n1 < n2:
    print('O segundo número ({}), é maior do que {} .'.format(n2, n1))
elif n1 == n2:
    print('Valores Iguais!!')
print('Fim do Programa!')
