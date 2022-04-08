"""
Crie um programa onde o usuário possa digitar vários valoes numéricos e
cadastre-os em uma lista.

Caso o número já exista lá dentro, ele não será adicionado.

No final, serã exibidos todos os valores únicos digitados, em ordem crescente.
"""
# Criando uma lista vazia
numeros = list()

# Criando um laço infinito
while True:
    # Criando uma variavel que receberá os inputs do usuário
    n = int(input('Digite um valor: '))
    # Se o input não estiver na lista, Será adicionado
    if n not in numeros:
        numeros.append(n)
        # Imprimindo mensagem
        print('Este valor será adicionado á lista.')
    # caso contrário, não faça nada.(O número não será adicionado)
    else:
        # Imprimindo msg alertando o usuário sobre o input repetido
        print('Valores duplicados não serão adicionados.')

    # Variável solicitante de continuação do programa
    r = str(input('Deseja continuar?\n'
                  '[Sim/Não]: ')).upper().strip()[0]

    # Condicional caso o usuário deseje encerrar o programa
    if r in 'Nn':
        # Interrompendo o programa
        break
# Imprimindo o nosso separador
print('-=' * 30)

# ordenando a nossa lista antes de imprimir
numeros.sort()
# Imprimindo a lista
print(f'Você digitou os valores {numeros}')
