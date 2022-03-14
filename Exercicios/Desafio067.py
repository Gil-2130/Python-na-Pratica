# Faça um programa que mostre a tabuada de vário números, um de cada vez.
# Faça isso para cada valor digitado.
#
# O programa será interrompido quando o numero solicitado for negativo

# variavel para armazenar o input
num = 0

# Variavel acumuladora
cont = 0

# Variavel para armazenar os resultados da tabuada
res = 0

# Enquanto for verdade
while True:
    # Solicitando o numero para o usuário
    num = int(input('Digite um número: '))
    print('--' * 20)
    # Condição para interromper o loop
    if num < 0:
         break

    # Criando um iterador para a tabuada
    for i in range(0,10):
        # contador
        cont = i + 1
        # Multiplicador
        res = num * cont
        # Imprimindo os resultados da tabuada
        print(f'{num} x {cont} = {res}')

# Mensagem de FIm do programa
print('Fim')
