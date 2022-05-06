"""
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organinzando
os dados em forma tabular.

"""
# Tupla de itens de uma cesta com os respectivos valores
cesta = ('leite:', 2.50,
         'café:', 5.80,
         'açucar:', 3.50,
         'arrox:', 10.0,
         'macarrão:', 3.50)

# Espaçadores tabulares (de acordo com a sua preferencia)
print('*' * 40)
print('{:-^40}'.format(' LISTAGEM de PRODUTOS e PREÇOS '))
print('*' * 40)

# Laço da posição do produto (pos-> posição)
for pos in range(0, len(cesta)):
    
    # Obtendo os elementos da posição 0
    if pos % 2 == 0:
        
        # Imprimindo os elementos 0 e 1 numa única linha
        print(f'{cesta[pos]:.<33}', end=' ')
        
    # Obtendo os elementos da posição 1
    else:
        print(f'{cesta[pos]:>.2f}','R$')
        
# Espaçador final da tabulação
print('*' * 40)
