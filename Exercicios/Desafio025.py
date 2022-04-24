"""
Crie um programa que leia o nome de uma pessoa e diga
se ela tem SILVA no nome.
"""

# Obtendo o nome da pessoa
nome = str(input('Qual o seu nome? ')).strip()
# Imprimindo resultados
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
