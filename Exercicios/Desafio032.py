"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

from datetime import date
ano = int(input('Qual ano deseja Analizar? \nDigite 0 para analisar o ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')  # Formatando de forma diferente pra não perder o costume
