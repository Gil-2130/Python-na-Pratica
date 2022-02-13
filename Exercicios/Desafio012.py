"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo
preço com 5% de desconto
"""
p1 = float(input('Digite o valor do Produto: '))
#p2 = p1-(p1*0.05)
p2 = p1 - (p1 * 5 / 100)
print('O novo valor com desconto é de {}$'.format(p2))
