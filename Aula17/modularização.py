"""
A modularização tem em suas premissas:
A) - Surgiu mo início da década de 60
B) - Sistemas ficando cada vez maiores
C) - Foco; dividir um programa grande
D) - Foco; Aumentar a legibilidade
E) - Foco; facilita a manutenção de código
F) - Organização do código
G) - Facilidade de manutenção
H) - Ocultação de código detalhado
I) - Reutilização em outros projetos
"""

# Exemplo 1
num = int(input('Digite um valor: '))

# importando módulo fatorial criado anteriormente
from uteis import numeros

fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')

print(f'O dobro de {num} é {numeros.dobro(num)}')
