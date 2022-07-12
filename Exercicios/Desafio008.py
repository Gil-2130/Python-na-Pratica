"""
Crie um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
"""

# Obtendo a metragem
met = float(input('Quantos metros deseja converter? '))

# Convertendo a metragem para centimetros
cent = met * 100

# Convertendo a metragem para milímetros
mili = met * 1000

# Imprimindo os resultados
print('O valor convertido em centimetros é {:.0f}cm'.format(cent))
print('=' * 20)
print('O valor convertido em milímetros é {:.0f}mm'.format(mili))

# Formatando melhor o print
print('A medida {}, corresponde a {:.0f}cm e {:.0f}mm'.format(met, cent, mili))
