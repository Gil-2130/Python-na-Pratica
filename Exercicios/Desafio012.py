"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo
preço com 5% de desconto
"""

# Obtendo o valor do produto
p1 = float(input('Digite o valor do Produto: '))
# Calculando o desconto (de duas maneiras)
#p2 = p1-(p1*0.05)
p2 = p1 - (p1 * 5 / 100)
# Imprimindo os resultados
print('O novo valor com desconto é de {}$'.format(p2))
