"""
Faça um programa que calcule a soma entre todos os numeros ímpares
que são multiplos de três e que se encontram no intervalo entre 1 até 500
"""
# Variavel acumuladora para guardar o resultado do laço
soma = 0

# Variável contadora para saber quantos números foram encontrados
cont = 0

# laço atendendo os requisitos do problemas
for i in range(1, 501):

    # Condicional para números ímpares e multiplos de 03
    if i % 3 == 0 and i % 2 == 1:

        # Com a condição atendida, iremos guardar o resultado na variavel (acumulador)
        soma = soma + i 
        
        # verificando quantos números foram obtidos (contador)
        cont = cont + 1

        # Este print não é necessário, então podemos remover.
        print(i)
        
# Por fim imprimimos os resultados
print('Foram encontrados {} números nessa sequência'.format(cont))
print('A soma total foi de {}'.format(soma))
