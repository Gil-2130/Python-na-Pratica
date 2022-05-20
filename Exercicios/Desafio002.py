"""
Exercício 2 ->Crie um Programa que eia o nome de uma pesooa de mostre uma mensagem de boas-vindas.

"""

# Respostas com várias saídas formatadas

# Obtendo o nome e armazenando em uma variável
nome = input('Qual é o seu nome? ')

# Imprimindo de várias formas diferentes
print(f'Olá {nome}, Seja Bem vindo(a) ao Python!')
print('============================')
print('Olá {}, Seja bem vindo!'.format(nome))
print('============================')
print('Seja Bem vindo',nome)
