"""
Crie um programa que tenha um tupla totalmente preenchida com uma
contagem por extenso de zero até 20.

Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso
"""


# Tupla contendo os numeros
num_0 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
         'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove',
         'Vinte')

# Enumerando os indices
num_1 = enumerate(num_0)

# Solicitando um indice ao usuário
num = int(input('Digite um numero entre 0 e 20:  '))

# laço para iterar sobre os indices
for i in num_1:

    #  Se o input estiver dentro do iterador
    if num in i:
        print(f'O numero digitado foi {num}\n'
              f'Escrito em extenso é: {i[1]}')

    # Se o input estiver fora do range do indice da lista/tupla
    if num < 0 or num > 20:
        print('Numero não permitido!!')
        break

# Solução do professor: (Porém para min não funcionou...)

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove',
        'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')
