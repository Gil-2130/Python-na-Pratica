"""
Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.
"""

# Formula 1
m = int(input('Digite um número: '))
one = m * 1
two = m * 2
three = m * 3
four = m * 4
five = m * 5
six = m * 6
seven = m * 7
eight = m * 8
nine = m * 9
ten = m * 10
print('A Tabuada 1 de {} é {}'. format(m, one))
print('A Tabuada 2 de {} é {}'. format(m, two))
print('A Tabuada 3 de {} é {}'. format(m, three))
print('A Tabuada 4 de {} é {}'. format(m, four))
print('A Tabuada 5 de {} é {}'. format(m, five))
print('A Tabuada 6 de {} é {}'. format(m, six))
print('A Tabuada 7 de {} é {}'. format(m, seven))
print('A Tabuada 8 de {} é {}'. format(m, eight))
print('A Tabuada 9 de {} é {}'. format(m, nine))
print('A Tabuada 10 de {} é {}'. format(m, ten))
print('=' * 20)
print('{} X 1  = {}'.format(m, one))
print('{} X 2  = {}'.format(m, two))
print('{} X 3  = {}'.format(m, three))
print('{} X 4  = {}'.format(m, four))
print('{} X 5  = {}'.format(m, five))
print('{} X 6  = {}'.format(m, six))
print('{} X 7  = {}'.format(m, seven))
print('{} X 8  = {}'.format(m, eight))
print('{} X 9  = {}'.format(m, nine))
print('{} X 10 = {}'.format(m, ten))
print('='*20)


# Formula 2 Simplificada usando laço de repetição
# Formula 2 Simplificada usando laço de repetição
n = int(input('Digite um numero: '))
for i in range(0, 11):
    j = i
    i = i * n
    print('{} X {} = {}'.format(n, j, i))
