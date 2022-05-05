"""

Desenvolva um programa que leia 04 valores pelo teclado
e guarde-os em uma tupla.

No final mostre:
A). Quantas vezes apareceu o valor 9
B). E que posição foi digitado o primeiro valor 3
C). Quais foram os números pares.
"""

# Criando uma tupla através de um input
num = (int(input('Digite um  número: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite outro número: ')),
       int(input('Digite o ultimo numero: ')))

# Imprimindo os valores digitados
print(f'Você digitou os valores {num}')

# Imprimindo o valor 9 caso ele esteja na tupla
print(f'O valor 9 apareceu {num.count(9)} vezes.' if 9 in num else 'O valor 3 não consta na tupla!')

# Imprimindo a posição do valor 3 se ele estiver na tupla
print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.' if 3 in num else 'O valor 3 não consta na tupla.')

# Imprimindo os valores pares
for x in num:
    if x % 2 == 0:
        print(f'Números pares encontrados: {x}')
    elif x % 2 == 1:
        print(f'Números ímpares encontrados: {x}')
