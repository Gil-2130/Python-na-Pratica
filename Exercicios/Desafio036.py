"""
Desenvolva um programa para aprovar um emprestimo bancário para a compra
de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.

calcule o valor da prestação mensal sabendo que ele não pode exceder
30% do salário ou então o empréstimo será negado.
"""

# Valor da casa
casa = float(input('Qual o valor da casa? '))

# Salário por Mês
salario = float(input('Qual é o seu salário? '))

# Quantidade de anos para pagamento
ano = float(input('Em quantos anos pretende pagar? ')) * 12

# Valor da prestação
prestação = casa / ano

# Calculando os 30% da prestação para pagamento
if prestação <= prestação * 0.30:
    print('Parabéns! Seu crédito foi aprovado!\n'
          'Sua prestação será de R${:.2f} mensais'.format(prestação))
else:
    print('Que pena! Não podemos aprovar sua solicitação!')
print('Obrigado pelo contato!')
