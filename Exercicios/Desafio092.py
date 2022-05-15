"""
Crie um programa que leia NOME, Ano de Nascimento e carteira de trabalho,
cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de 0,
o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa irá se aposentar.
"""
# Importando biblioteca para trabalhar com datas
from datetime import datetime

# Criando um dicionário
dados = dict()
# Adicionando dados aos dicionários(nome, idade, CTPS
dados['Nome'] = str(input('Digite o seu Nome: '))
nasc = int(input('Digite o seu ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Nº Carteira de Trabalho(0 não possui): '))

# Condicional caso o usuário possua carteira de trabalho
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Último Salário: '))
    # calculando aposentadoria
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)

print('-=' * 30)

# Fazendo um laço para obter os dados
for key, value in dados.items():
    print(f'    = {key} tem o valor {value}')
