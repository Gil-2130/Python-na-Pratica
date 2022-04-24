"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos digitos separados.
EX;
Digite um numero: 1834
UNIDADE : 4
DEZENA : 3
CENTENA: 8
MILHAR: 1
"""

# Solicitado o input ao usuário
n1 = int(input('Digite um numéro entre 0 e 9999: '))
# Calculando a unidade
u = n1 // 1 % 10
# Calculando as dezenas
d = n1 // 10 % 10
# Calculando as centenas
c = n1 // 100 % 10
# calculando os milhares
m = n1 // 1000 % 10

# Imprimindo resultados
print('UNIDADE: {}'.format(u))
print('DEZENA: {}'.format(d))
print('CENTENA: {}'.format(c))
print('MILHAR: {}'.format(m))
