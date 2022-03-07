"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro
de fogos de artificio, indo de 10 até 0, com um pausa de 1 segundo entre eles.
"""

# Importando módulo para pausar a contagem regessiva
from time import sleep

# laço de contagem regressiva
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('Bummm!!...Bumm!!..Bumm..!!')
