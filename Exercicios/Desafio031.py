"""
Desenvolva um programa que pergunte a distância de uma viagem em KM.

Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km
e R$0,45 para viagens mais longas.
"""

# Forma 1
viagem = float(input('Quantos quilômetros tem a viagem? '))
if viagem <= 200:
    print('O preço da passagem custará R${}'.format(viagem * 0.50))
else:
    print('O preço da passagem custará R${}'.format(viagem * 0.45))

print('_==_' * 20)

# forma 2
viagem_1 = float(input('Quantos KM tem a viagem? '))
print('Você está prestes a iniciar uma viagem de {}Km'.format(viagem_1))
if viagem_1 <= 200:
    preço = viagem_1 * 0.50
else:
    preço = viagem_1 * 0.45
print('E o preço da sua passagem será {}'.format(preço))


# ou
#preco = viagem_2 * 0.50 if  viagem_2 <= 200 else viagem_2 *0.45
# essa é uma forma válida, porém pode se tornar algo confuso para interpretação.
