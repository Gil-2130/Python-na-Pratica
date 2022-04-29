"""

Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.

"""

# Inicializando variaveis que irão armazenar peso minimo e máximo
p_max = 0
p_min = 0
# Criando laço para solicitar o peso das pessoas (5)
for i in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))

    # Condicionais
    if i == 1:
        p_max = peso
        p_min = peso

    else:
        if peso > p_max:
            p_max = peso
        elif peso < p_min:
            p_min = peso


print('O maior peso lido foi {}Kg'.format(p_max))
print('O menor peso lido foi {}Kg'.format(p_min))
