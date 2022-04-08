"""
Faça um programa que leia 05 valores numéricos e guarde em uma lista.

No final mostre; Qual foi o menor e maior valor digitado e as suas respectivas
posições na lista
"""
# Criando uma lista vazia
valores = []

# laço para solicitar um range de inputs
for i in range(0, 5):
    # Adicionando os inputs à lista vazia
    valores.append(int(input('Digite um valor: ')))

# Imprimindo a lista
print(f'Os valores digitados foram: {valores}')

# Encontrando o maior valor e em qual indice ele se encontra
print(f'O maior valor encontrado foi {max(valores)},\n',
      f'O valor está no indice {valores.index(max(valores))}')

# Encontrando o menor valor e em qual indice ele está
print(f'O menor valor encontrado foi {min(valores)},\n',
      f'O valor está no indice {valores.index(min(valores))}')
