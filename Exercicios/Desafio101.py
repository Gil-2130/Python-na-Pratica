'''

Crie um programa que tenha uma função chamada voto()
Esta irá receber como parâmetro o ano de nascimento de uma pessoa.
Retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

'''


# Criando função
def voto(ano):
    # importando biblioteca para trabalhar com datas
    from datetime import date

    # obtendo ano atual
    atual = date.today().year

    # Calculando idade
    idade = atual - ano

    # Condicionas de obrigatoriedade de votação
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


# Obtendo a idade do usuário
nasc = int(input('Em que ano você nasceu?: '))

# Imprimido programa
print(voto(nasc))
