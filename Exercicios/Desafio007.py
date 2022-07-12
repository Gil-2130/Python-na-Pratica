"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
"""

# Obtendo e armazenando a primeira nota
nota1 = int(input('Qual foi a primeira nota? '))

# Obtendo e armazenando a segunda nota
nota2 = int(input('Qual foi a segunda nota? '))

# Calculando a média
media = (nota1 + nota2) / 2

# Imprimindo os resultados
print('A nota média foi de {}'.format(media))
