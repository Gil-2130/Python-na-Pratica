"""
Escreva um programa que converta uma temperatura
digitada em ℃ e converta para ℉
"""
temp = float(input('Qual a temperatura hoje em ℃? '))
fah = temp * 1.8 + 32

# OU
# fah = temp * 9 / 5 + 32
print('A temperatura em Fahrenheit é de {}℉'.format(fah))

temp1 = float(input('Qual a temperatura hoje em ℉? '))
cels = (temp1 - 32) / 1.8
print('A temperatura em Celsius é de {}℃'.format(cels))