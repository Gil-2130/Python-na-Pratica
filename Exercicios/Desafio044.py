"""
Elabore um programa que calcule o valor a ser oago por um produto,
considerando o seu preço normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- Em até duas vezes no cartão: Prço normal.
- 3x ou mais no cartão: 20% de juros
"""

if opcao == 1:
    desconto = product - product * 0.10
    print('Seu desconto será R${}, o valor total será de R${}'.format(product - desconto, desconto))
elif opcao == 2:
    desconto = product - product * 0.05
    print('Seu desconto será de R${} e o preço total será de R${}'.format(product - desconto, desconto))
elif opcao == 3:
    print('Você pagará duas parcelas iguais de R${}'.format(product / 2))
elif opcao == 4:
    juros = product + product * 0.20
    print('O valor total será de R${} e você pagará R${:.2f} por Mês.'.format(juros, juros / 3))
