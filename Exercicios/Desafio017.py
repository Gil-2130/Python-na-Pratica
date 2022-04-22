"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triangulo retangulo, calcule e mostre o compriento da hipotenusa.
"""

# A minha Resposta (Importando Módulo)
from math import sqrt, trunc
# Obtendo o cateto oposto
cat_ops = float(input('Qual o valor do cateto oposto?: '))
# Obtendo o cateto adjacente
cat_adj = float(input('Qual é o valor do cateto adjacente? '))
# Obtendo a Hipotenusa
hipo_x = sqrt(pow(cat_ops, 2) + pow(cat_adj, 2))
# Imprimindo resultados
print('O valor da Hipotenusa é {:.2f}'.format(hipo_x))
print('=' * 20)

# Resposta do professor (Sem módulo)
co = float(input('Comprimento do catetto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co**2 + ca**2) ** (1/2)
print('A Hipotenusa vai medir {:.2f}'.format(hi))
print('=' * 20)


# Calculo de hipotenusa disponivel em python
from math import hypot
cat_ops = float(input('Comprimento do cateto oposto: '))
cat_adj = float(input('Comprimento do cateto adjacente: '))
hipo = hypot(cat_ops, cat_adj)
print('A hipotenusa mede {:.2f}'.format(hipo))
