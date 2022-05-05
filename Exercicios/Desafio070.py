"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final mostre;

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais vendido?
"""

# variaveis para armazenar valores
total = 0
totmil = 0
p_menor = 0
cont = 0
p_barato = ''

# Enquanto a condição for verdadeira
while True:
    produtos = str(input('Digite um produto: '))
    preco = float(input('Qual o valor do produto? R$'))
    total = total + preco

    if preco > 1000:
        totmil = totmil + 1

    if cont == 1:
        p_menor = preco
        p_barato = produtos
    else:
        if preco < p_menor:
            p_menor = preco
            p_barato = produtos

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar?\n'
                         '[S/N] ')).strip().upper()[0]

    if resp in 'Nn':
        break

print('{:=^40}'.format(' FIM do PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {p_barato} e custa R${p_menor:.2f}')
