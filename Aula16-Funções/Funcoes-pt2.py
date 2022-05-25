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

# ========= ESCOPO DE VARIÁVEIS ===========

# Criando uma variável GLOBAL(Acessível/Visível dentro e fora de funções)
n = 2


def teste():
    # Esta é uma variável LOCAL(acessível/Visível apenas na função)
    x = 8
    # Imprimindo a variável GLOBAL
    print(f'Na função, n vale {n}.')
    # Imprimindo a variável LOCAL
    print(f'Na função, x vale {x}.')


print(f'No programa principal n vale {n}')
# Imprimindo a função
teste()


# print(f'No programa principal x,vale {x}')
# Perceba que x não foi impresso, pois, ele está disponível apenas na função,
# e não fora dela. Isso se chama escopo de variável (LOCAL/GLOBAL)


# EXEMPLO 2
def teste_2(b):
    b = b + 4
    c = 2
    print(f'A dentro da função vale {a}')
    print(f'B dentro da função vale {b}')
    print(f'C dentro da função vale {c}')


# programa principal
a = 5
teste_2(a)

# Observação IMPORTANTE:
''' Se existir uma variavel global e outra local com o mesmo nome,
ambas não terão seus valores sobrescritos pois estão em escopos diferentes.
Isto quer dizer se imprimirmos A dentro da função ou fora dela, será impresso
apenas o valor correspondente ao escopo (global ou local)
Vejamos o EXEMPLO 2 modificado logo abaixo'''


# EXEMPLO 2 MODIFICADO
def teste_2a(b):
    # Podemos usar A GLOBAL da seguinte forma:
    global a
    a = 8
    '''O A veio de fora com valor 5, mas foi alterado para outro quando
    alteramos seu valor dentro da função
    '''
    b = b + 4
    c = 2
    print(f'A dentro da função vale {a}')
    print(f'B dentro da função vale {b}')
    print(f'C dentro da função vale {c}')


# programa principal
a = 5
print(f'A fora da função vale {a}')
teste_2a(a)


# ========= RETORNO DE VALORES(return) =========
def somar(d=0, e=0, f=0):
    s = d + e + f
    return f'\nA soma vale {s}'


r1 = somar(10, 5, 6)
r2 = somar(10, 5)
r3 = somar(5, 6)
print(r1, r2, r3)


# EXEMPLO PRÁTICO
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f = f * c
    return f


# Imprimindo resultados A
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')


# Imprimindo resultados B
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(6)
print(f'os resultados fatoriais são {f1}, {f2} e {f3}')


# função de par
def par(num= 0):
    if num % 2 ==0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
if par(n):
    print(f'{n} é par')
else:
    print(f'{n} Não é par')
