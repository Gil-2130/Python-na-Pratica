"""
Escreva um programa que converta uma temperatura
digitada em ℃ e converta para ℉
"""
# Obtendo a temperatura em Celsius
temp = float(input('Qual a temperatura hoje em ℃? '))
# Calculando e convertendo para Fahrenheit
fah = temp * 1.8 + 32

# Método 2
# fah = temp * 9 / 5 + 32
print('A temperatura em Fahrenheit é de {}℉'.format(fah))
# Obtendo a temperatura
temp1 = float(input('Qual a temperatura hoje em ℉? '))
# Convertendo
cels = (temp1 - 32) / 1.8
print('A temperatura em Celsius é de {}℃'.format(cels))
