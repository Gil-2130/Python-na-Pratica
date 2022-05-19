"""

Faça um programa que tenha uma função chamada área().
A mesma deverá receber as dimensões de um terreno retangular(largura e comprimento)
Depois imprima a área do tereno

"""


# Criando função para calcular a área de um terreno
def area(largura, comprimento):
    # calculando a área
    a = largura * comprimento
    # Imprimindo resultados
    print(f'A área de um terreno {largura} X {comprimento} é de {a}m².')


print(' Calculo de Área do Terreno!')
print('-' * 20)
# Obtendo a largura
l = float(input('Digite a largura do terreno(Mts): '))
# Obtendo o comprimento
c = float(input('Agora digite o comprimento(Mts): '))
# chamando a função para imprimir os resultados
area(l, c)
