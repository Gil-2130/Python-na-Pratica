"""
Crie um programa que leia um valor em metros e o exiba convertido em centimetros
 e milimetros
"""
met = int(input('Quantos metros deseja converter? '))
cent = met * 100
mili = met * 1000
print('O valor convertido em centimetros é {}cm'.format(cent))
print('=' * 20)
print('O valor convertido em milímetros é {}mm'.format(mili))