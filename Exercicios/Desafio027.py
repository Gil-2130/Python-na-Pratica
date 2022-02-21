"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o ultimo nome separadamente
EX:
ANA Maria de Souza
Primeiro nome: Ana
Ultimo Nome: Souza
"""
nome = 'Ana Maria de Souza'
print(nome[0:3], nome[13:18])

# OU
nome_1 = str(input('Digite o seu nome: ')).strip()
fr = nome_1.split()
print('Seu prmeiro nome é {}'.format(fr[0]))
print('Seu ultimo nome é {}'.format(fr[-1]))