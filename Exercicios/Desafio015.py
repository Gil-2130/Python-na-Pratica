"""
Escreva um Programa que pergunte a quantidade de KM percorridos por um carro alugado e
a quantidade de dias que ele foi alugado.

Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por kilometro rodado
"""
# Obtendo aquilometragem
kilometros = float(input('Quantos kilômetros você rodou com o veículo? '))
# Obtendo a quantidade de dias utilizados
dias_rodados = float(input('Quantos dias o veículo foi alugado? '))
# Calculando o valor a pagar
total_pagar = (0.15 * kilometros) + (60* dias_rodados)
# Imprimindo resultados
print('Você rodou {}KM por {:.0f} dias.\n'
      'Sendo assim o custo total será de {}$'.format(kilometros, dias_rodados, total_pagar))

