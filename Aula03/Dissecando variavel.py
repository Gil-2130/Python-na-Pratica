"""

Identificando o tipo de dado que recebemos no input e todos os métodos disponiveis

A saída será um boolean.
"""

a = input('Digite algo: ')

print('O tipo primitivo deste dado é', type(a))
print('Possui espaços? ', a.isspace())
print('Pode ser convertido para numero? ', a.isdigit())
print('É um dado alafabetico? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('É um dado capitalizado? ', a.istitle())
print('É um numero? ', a.isnumeric())
