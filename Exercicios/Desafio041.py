"""
A confederação de natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

 - Até 9 anos: MIRIM
 - Até 14 anos: INFANTIL
 - Até 19 anos: JUNIOR
 - Até 20 anos: SÊNIOR
 - Acima de 20 anos: MASTER
"""

# Importando módulo para trrabalhar com datas
from datetime import date

# obtendo a data atual
atual = date.today().year

# obtendo ano de nascimento
ano_nasc = int(input('Ano de Nascimento: '))

# obtendo a idade
idade = atual - ano_nasc

# Condicional para categorização MIRIM
if idade <= 9:
    print('Você nasceu em {} e tem {} anos de idade.\n'
          'Sua categoria é MIRIM.'.format(ano_nasc, idade))

# Condicional para categorização INFANTIL
elif idade <= 14:
    print('Você nasceu em {} e tem {} anos de idade.\n'
          'Sua categoria é INFANTIL.'.format(ano_nasc, idade))

# Condicional para categorização JÚNIOR
elif idade <= 19:
    print('Voçê nasceu em {} e tem {} anos de de idade.\n'
          'Sua categoria é JÚNIOR.'.format(ano_nasc, idade))

# Condicional para categorização SÊNIOR
elif idade <= 20:
    print('Você nasceu em {}  e tem {} anos de idade.\n'
          'Sua categoria é SÊNIOR.'.format(ano_nasc, idade))

# Condicional para categorização MASTER
elif idade > 20:
    print('Você nasceu em {} e tem {} anos de idade.\n'
          'Sua categoria é MASTER'.format(ano_nasc, idade))
