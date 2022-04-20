"""
Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor
"""
# Obtendo um número pelo input e armazenando em uma variável
n = int(input('Digite um número: '))
# Calculando o antecessor do input
ant = n - 1
# calculando o sucessor do input
suc = n + 1
# Imprimindo os resultados
print('O antecessor de {} é {} e o sucessor é {}'.format(n, ant, suc))

# Simplificando o codigo
n1 = int(input('Digite um numero: '))
print('O antecessor de {} é {}, e o sucessor é {}'.format(n1, (n1 - 1), (n1 + 1)))
