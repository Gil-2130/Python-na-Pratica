# Exemplo de criação de uma função simples para imprimir linha
def mostralinha():
    print('--------------------------------------------')


# Fazendo um chamado á função...
mostralinha()
# Imprimindo uma msg qualquer
print('             SISTEMA DE ALUNOS           ')
mostralinha()
print('         CADASTRO DE FUNCIONÁRIOS            ')

print('======== SEPARADOR DE LINHAS ========')


# Criando função que recebe um parâmetro
def mensagem(msg):
    print('===============================================')
    print(msg)  # Parâmetro
    print('===============================================')


mensagem('              SISTEMA de ALUNOS                  ')
mensagem('         CADASTRO DE FUNCIONÁRIOS            ')


# =========================== PRÁTICA ===================================

# Operações aritméticas básicas (SOMA)
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 3
s = a + b
print(s)


# Criando função de soma
def soma(a, b):
    s = a + b
    print(s)


# Criando função de multiplicação
def mult(a, b):
    m = a * b
    print(m)


# Função de divisão
def div(a, b):
    print(f'Divisão A=>{a} por B=>{b}')
    d = a / b
    print(f'A divisão de {a} por {b} é igual a {d:.0f}')


# Programa principal
soma(4, 5)
soma(5, 10)

mult(5, 10)

div(10, 5)

soma(a=20, b=15)  # Dizendo explicitamente os parâmetros (pode-se mudar a ordem, mas não esqueça de explicitar todos.)


# Conceito de empacotar parâmetros
def contador(*num):  # asterisco significa um número ilimitado de parâmetros
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

    # for valor in num:
    #     tam = len(num)
    #     print(f'Recebi os valores {num} e são ao todo {tam} números!')
    #     #print(valor, end=' ')
    # #print(f'...FIM!!  temos {tam} elementos.')


contador(2, 1, 7)
contador(8, 0)
contador(1, 4, 8, 9, 6)

# Trabalhando com listas
valores = [7, 2, 5, 0, 4]


# Função que realiza o dobro de cada valor inputado na lista
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] = lista[pos] * 2
        pos = pos + 1


print(f'Os valores originais são {valores}')
dobra(valores)
print(f'Os valores modificados com a função agora são {valores}')


# Criando novamente a função de soma, mas com parâmetros indefinidos
def Soma(*valores):
    s = 0
    for num in valores:
        s = s + num
    print(f'A soma dos valores {valores} temos {s}')


Soma(5, 2)
Soma(5, 10, 15)
