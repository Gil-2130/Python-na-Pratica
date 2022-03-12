"""
Crie um programa que leia 02 valores e mostre um menu na tela;
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa

O programa deverá realizar a operação solicitada em cada caso.
"""
# Importando modulo tempo apenas para dar um 'lazy' no ultimo print
from time import sleep

# armazenando a operação
oper = 0

# Enquanto a operação for diferente de 5(sair)
while oper != 5:

    # Solicitando 02 numeros ao usuário
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))

    # Separação de print e input
    print('-=-' * 20)

    # Solicitando operação ao usuário
    oper = int(input('Qual operação deseja fazer?\n'
                     '[1] Soma\n'
                     '[2] Multiplicação\n'
                     '[3] Maior\n'
                     '[4] Novos números\n'
                     '[5] Exit\n'
                     'Opção escolhida: '))

    # Separando o print
    print('-=-' * 20)

    # condicionais das operações do menu do programa
    # Adição
    if oper == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
        print('-=-' * 20)

    # Multiplicação
    elif oper == 2:
        mult = num1 * num2
        print('{} x {} = {}'.format(num1, num2, num1 * num2))
        print('-=-' * 20)

    # Verificando qual é o maior número
    elif oper == 3:
        print('O maior valor entre {} e {}, é {}'.format(num1, num2, max(num1, num2)))
        print('-=-' * 20)

    # Solicitando novos inputs
    elif oper == 4:
        print(num1, num2)
        print('-=-' * 20)

    # Atendendo a solicitação para encerrar o programa
    elif oper == 5:
        print('Encerrando o programa...')
        sleep(1)

    # Caso o usuário digite alguma opção fora do menú
    else:
        print('Opção Inválida!!!')

# Fim do programa
else:
    print('FIM')


# RESPOSTA do Professor
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))

opcao = 0

while opcao != 5:
    print('''[ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos Números
        [ 5 ] Sair do Programa''')

    opcao = int(input('Qual a sua opção?  '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))

    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} * {} é {}'.format(n1 ,n2, mult))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior ))

    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(int('Segundo Valor: '))

    elif opcao == 5:
        print('Fializando...')

    else:
        print('Opção Inválida!!!')
    print('=-='*10)

print('Fim do Programa!!')
