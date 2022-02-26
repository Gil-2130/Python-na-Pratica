"""
Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%

Para os inferiores ou iguais, aumento é de 15%
"""

salario = float(input('Qual é o seu salário? '))
if salario <= 1250:
    print('OK, seu atual salario de R${} sofrerá reajuste de 15%\n'.format(salario),
          'Seu novo salário será de R${}'.format(salario + (salario * 0.15)))
else:
    print('OK, seu atual salario de R${} sofrerá reajuste de 10%\n'.format(salario),
          'Seu novo salário será de R${}'.format(salario + (salario * 0.10)))
    
    # OU
if salario <= 1250:
    novo = salario + (salario * 15 / 100)  # mesma coisa que salario * 0.15
else:
    novo = salario + (salario * 10 / 100)
print('Seu salário antigo era R${} , seu novo salário é R${}'.format(salario, novo))
