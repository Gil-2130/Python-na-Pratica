"""
    Laço de repetição FOR(finito)
  
"""

# Imprimindo  "OI" 06 vezes (improdutivo)
print('oi')
print('oi')
print('oi')
print('oi')
print('oi')
print('oi')

# Separacao dos prints
print('{:=^50}'.format(' ESPAÇO ENTRE PRINTs '))

# Imprimindo  "OI" 06 vezes usando estrutura de repetição
for c in range(1, 7):
    print('OI')
print('FIM')

# Separando os prints
print('{:=^50}'.format(' ESPAÇO ENTRE PRINTs '))

# Imprimindo um range de 10 números
for c in range(0, 11):
    print(c)

# Separando os prints
print('{:=^50}'.format(' ESPAÇO ENTRE PRINTs '))


# Laço de repetição invertido
for c in range(10, 0, -1):  # laço invertido do 10 a 0 em ordem decrescente
    print(c)



# Separando os prints
print('{:=^50}'.format(' ESPAÇO ENTRE PRINTs '))



# Laço de repetição pulando uma determinada casa de numeros
for c in range(0, 11, 2):  # De 0 a 11 pulando de 2 em 2
    print(c)



# Separando os prints
print('{:=^50}'.format(' ESPAÇO ENTRE PRINTs '))



# Criando um laço com o input do usuario
n = int(input('Digite um número: '))

for c in range(0, n, 2):  # pulando de dois em dois
    print('Número {}'.format(c))



# Separando os prints
print('{:=^50}'.format(' ESPAÇO ENTRE PRINTs '))



# Criando um laço com o input do usuario
n = int(input('Digite um número: '))
for c in range(0, n + 1):  # adicionando mais um contador ao input (util se desejar adicionar o exclusivo)
    print('Número {}'.format(c))

# criando um schema de como funciona o laço
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f + 1, p):  # inicio, fim + 1 e o passo
    print(c)

# Separando os prints
print('{:=^50}'.format(' ESPAÇO ENTRE PRINTs '))

# Laço de repetição de um input
for c in range(0, 5):
    print(int(input('Digite um número: ')))

# Separando os prints
print('{:=^50}'.format(' ESPAÇO ENTRE PRINTs '))

# Usando o laço de repetição para somar valores do input
s = 0
for c in range(0, 4):  # Quantidade solicitada de inputs
    n = int(input('Digite um número: '))
    s = s + n  #pegando os valores da variavel N e guardando em s, no fim fazendo as somas entre valores.
print('O somatório de todos os valores foi {}'.format(s))
