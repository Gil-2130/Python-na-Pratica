"""
A confederação de natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

 - Até 9 anos: MIRIM
 - Até 14 anos: INFANTIL
 - Até 19 anos: JUNIOR
 - Até 20 anos: SÊNIOR
 - Acima de 20 anos: MASTER
"""

idade = int(input('Qual é a sua idade? '))
if idade <= 9:
    print('MIRIM é a sua categoria.')
elif idade > 9  and idade <= 14:
    print('INFANTIL é a sua categoria.')
elif idade > 14 and idade <= 19:
    print('JUNIOR é a sua categoria')
elif idade == 20:
    print('SÊNIOR é a sua categoria.')
elif idade > 20:
    print('MASTER é a sua categoria.')
