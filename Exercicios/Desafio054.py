"""
Crie um programa que leia o ano de nascimento de 07 pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

# Importando módulo para trabalhar com datas
from datetime import date

# data atual
ano_atual = date.today().year

# guardando a quantidade de pessoas adultas em uma variavel
t_maior = 0

# Guardando a quantidade pessoas jovens em outr a variavel
t_menor = 0

# criando um laço para solicitar vários inputs e idades diferentes
for pessoa in range(1, 8):

    # Solicitando ano de nascimento da pessoa
    ano_nasc = int(input('Digite a data de nascimento da {}ª pessoa? '.format(pessoa)))

    # Calculando a idade baseando-se no ano atual e ano de nascimento
    idade = ano_atual - ano_nasc

    # Condicional para maioridade atingida ou não (18 anos no caso do brasil)
    if idade >= 18:
        print('Essa pessoa é adulta')
        t_maior = t_maior + 1

    else:
        print('Essa pessoa ainda é jovem!')
        t_menor = t_menor + 1
        
# separando os prints acima para melhor visualização
print('-=-'*30)
print('No total tivemos {} pessoas adultas.\n'
      'No total tivemos {} pessoas jovens.'.format(t_maior, t_menor))
