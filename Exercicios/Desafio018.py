"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno
e tangente desse angulo.

Angulos mais usados (notáveis);

angulo      seno    Cosseno     Tangente
30°          1/2        √3/2      √3/3
45°          √2/2        √2/2 = 0,70       1
60°          √3/2         1/2      √3
"""


# Importando o seno, cosseno, tangente e radians(funçaõ para converção de centímetros)
from math import sin, radians, cos, tan

# qual o angulo?
angulo = float(input('Digite o angulo que você deseja usar: '))

# Calculando e imprimindo o SENO
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))

# Calculando e imprimindo o COSSENO
cosseno = cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))

# Calculando  e imprimindo a TANGENTE
tangente = tan(radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
