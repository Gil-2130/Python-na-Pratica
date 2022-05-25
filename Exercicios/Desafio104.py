'''

Crie um programa que tenha a função leiaINT(), que vai funcionar de forma semelhante à
função input() do Python, só ue fazendo a validação aceitar apenas um valor numérico.
EX:
n = leiaINT('Digite um numero: ')

'''


# Criando função
def leiaINT(msg):
    # Inicializando variável booleana de valor FALSO
    ok = False
    # Inicializando variável de valor zero
    valor = 0
    # laço infinito que receberá valores inteiros
    while True:
        # Obtendo os valores
        numero = str(input(msg))
        # Condicional se o valor digitado é um inteiro
        if numero.isnumeric():
            # Variável VALOR agora receberá o inteiro digitado
            valor = int(numero)
            # Variável booleana OK receberá valor TRUE
            ok = True
        # caso contrário...
        else:
            # imprimindo msg solicitando um valor inteiro ao usuário
            print(f'\033[0;31mERRO! Valor digitado inválido! Digite apenas números.\033[m')
        # Condicional para interromper o loop infinito
        if ok:
            break
    return valor


# Programa principal
numero = leiaINT('Digite um número: ')
print(f'Você digitou {numero}.')
