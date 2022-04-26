""" Faça um programa que leia o ano de nascimento de uma
pessoa e informe de acordo com a sua idade;
 - Se ele ainda vai se alistar ao serviço militar.
 - Se é hora de se alistar
 - Se já passou do tempo de se alistamento.

 O programa ainda deverá mostrar o tempo que falta ou que passou do prazo
"""

# importando biblioteca para trabalhar com datas
from datetime import date

# Obtendo o ano atual
atual = date.today().year

# Obtendo o ano de nascimento
nasc = int(input('Digite o seu ano de nascimento? '))

# Obtendo o sexo da pessoa
sexo = str(input('Qual o seu sexo? ').lower())

# Calculando a idade
idade = atual - nasc

# Idade para alistamento
alist = 18

# Condicional para alistamento (sexo F)
if sexo == 'f':
    print('Mulher, você não é obrigada a se alistar!')

 # 
 elif sexo == 'm':
    print('Homens são obrigados a se alistar!')
elif idade < 18:
    print('Faltam {} anos para se alistar no serviço militar.'.format(alist - idade))
    saldo = 18 - idade
    print('Seu alistamento será em {}'.format(atual + saldo))
elif idade == 18:
    print('É hora de se alistar!')
elif idade > 18:
    print('Você já passou {} anos da data limite de alistamento!'.format(idade - alist))
print('Bem vindo ao serviço militar!')

