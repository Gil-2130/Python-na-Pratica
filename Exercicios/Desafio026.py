"""
Crie um programa que leia uma frase pelo teclado e mostre:
1. Quantas vezes aparece a letra A
2. Em que posição ela aparece a primeira vez.
3. Em que posição ela aparece a ultima vez
"""

frase = str(input('Digite qualquer frase: ')).strip()

# Quantas vezes a letra aparece na frase
print('A letra A aparece {} vezes na frase.'.format(frase.lower().count('a')))

# Posição que ela aparece a primeira vez
print('Letra A aparece primeiro no indice {}'.format(frase.lower().find('a')))

# posição que ela aparece a ultima vez
print('Letra A aparece pela ultima vez no Indice {}'.format(frase.lower().rfind('a')))
