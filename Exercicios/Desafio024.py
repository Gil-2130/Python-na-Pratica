"""
Crie um programa que leia o nome de uma cidade e diga se
ela começa ou não com o nome 'SANTO'
"""

cid_3 = str(input('Qual a sua cidade? ')).strip()  # REmovendo os espaços em excesso se eles existirem

# Verificando se a palavra digitada corresponde, porém devido ao case sensitive
# pegamos o input, colocamos em maiusculo e fazemos a comparação
print(cid_3[:5].upper() == 'SANTO')
