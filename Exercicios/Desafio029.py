"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma msg dizendo que ele foi multado.

A multa irá custar R$7,00 por cada km acima do limite.

"""

# Obtendo velocidade
vel = float(input('Qual é a velocidade do veículo? '))
# Definindo limite de velocidade
lim = 80
# Condicional para aplicação de multa e seu respectivo valor
if vel > 80:
    # Calculando o valor da multa
    mult = (vel - lim)*7
    # Imprimindo resultados
    print('Você foi MULTADO! O valor da multa será R${:.0f}'.format((mult)))
    
else:
    print('Muito bem! Respeite o limite de velocidade.')
