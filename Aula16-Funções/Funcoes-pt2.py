# Obtendo ajuda no Python(Interactive HELP)
print(input.__doc__)
help(input)


# Docstrings
def contador(i, f, p):
    # Para criar uma Dostring, apenas digite 03 aspas simples após a criação da função
    """
     Faz uma contagem e imprime na tela os resultados
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: passo da contagem diferente de 0
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c = c + p
    print('FIM')


contador(2, 10, 2)

help(contador)


# Parâmetros Opcionais
def somar(a, b, c=0):
    # podemos usar também todos os argumentos opcionais.
    # somar(a=0, b=0, c=0)
    """
    -> Função de Soma de 02 elementos
    :param a: Primeiro argumento
    :param b: Segundo argumento
    :param c: Terceiro argumento se houver
    :return: Sem Retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(2, 3, 5)
help(somar)
