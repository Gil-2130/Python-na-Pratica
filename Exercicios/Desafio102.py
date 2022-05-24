'''

Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
A) O primeiro que indique o número a calcular
B) O segundo será um valor lógico chamado SHOW, indicando se será mostrado
ou não na tela o processo de calculo do fatorial.

'''


# Criando função fatorial
def fatorial(numero, show=False):
    # Criando Docstring
    """
     -> Calcula o fatorial de um número.
    :param numero: Número a ser calculado.
    :param show: Parâmetro para exibir a operação executada.
    :return: Resultado da operação.
    """
    # Valor do fatorial
    fat = 1
    for contador in range(numero, 0, -1):
        # Condicional para mostrar  o fatorial sexecutado
        if show:
            print(contador, end='')
            if contador > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')

        fat = fat * contador
    return fat


# Programa principal
print(fatorial(5, show=True))
