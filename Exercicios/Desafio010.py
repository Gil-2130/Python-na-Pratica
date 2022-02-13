"""
Crie um programa que leia o quanto dinheiro uma pessoa tem na carteira
e mostre quantos dolares ela pode comprar
"""

# 1 Dólar (EUA) = 5,26 Real Brasileiro

reais = float(input('Quantos reais você tem na carteira? R$'))
dolar = reais / 5.26
print('Você com {}R$ Reais poderia comprar {:.2f}R$'.format(reais, dolar))
