"""
Faça um programa que tenha uma função chamada escreva(),
a mesma receberá um text qualquer como parâmetro e irá imprimir a mensagem
com tamanho adaptável.
"""


# Criando função
def escreva(msg):
    # adaptando o tamanho da msg
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa principal
escreva('Python é incrível!!')
