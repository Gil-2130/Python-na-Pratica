"""

  Importando modulos para calculos numericos (math)
  sqrt => Raíz quadrada
  ceil => Arredondar pra cima 5.8 -> 6.0
floor => Arredondar pra baixo 5.8 -> 5.0
trunc => truncate, corta na virgula/ponto sem arredondar 5.8 -> 5
pow => potência ou **
sqrt => Raiz quadrada
factorial =>

obs; Ao importar math e desejarmos usar uma ou mais funções, é necessário usar; math.funçao desejada.
Caso contrário, você pode importar apenas as funções desejadas usando o método FROM
"""

# importando o modulo completo (Necessário se for usar mais de 02 funções ou todas)
import math

num_1 = int(input('Digite um numero: '))
raiz_1 = math.sqrt(num_1)

print('A raiz de {} é igual a {}'.format(num_1, raiz_1))
print('A raiz de {} é igual a {}'.format(num_1, math.ceil(raiz_1)))  # arredondando numero pra cima
print('A raiz de {} é igual a {}'.format(num_1, math.floor(raiz_1)))  # Arredondando pra baixo

# importando apenas uma função do modulo(usado se for importar poucas funções apenas)
from math import sqrt, ceil, floor

num_2 = int(input('Digite um número: '))
raiz_2 = sqrt(num_2)
print('A raiz de {} é igual a {}'.format(num_2, raiz_2))
print('A raiz de {} é igual a {}'.format(num_1, ceil(raiz_1)))  # arredondando numero pra cima
print('A raiz de {} é igual a {}'.format(num_1, floor(raiz_1)))  # Arredondando pra baixo

# GErando numeros aleatorios
import random

num_3 = random.random()
print(num_3)
