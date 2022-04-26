"""
Crie um programa que leia 02 notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo coma média atingida:

 - Média abaixo de 5: REPROVADO
 - Média entre 5 e 6.9: RECUPERAÇÃO
 - Média 7 ou superior: APROVADO
"""

# Obtendo as notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digie a segunda nota: '))

# Calculando a média
media = (n1 + n2) / 2
# Condicional para aprovação
if media < 5:
    print('REPROVADO! Estude mais')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO! Cuidado, você deve melhorar.')
elif media >= 7:
    print('PARABÈNS! Você foi aprovado!')
