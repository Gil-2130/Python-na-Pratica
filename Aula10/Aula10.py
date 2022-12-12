"""
    Laço de Repetição WHILE(infinito)
"""

# Criando um laço de repetição simples com o FOR
for c in range(1, 10):
    print(c)
print('FIM!!')

# Criando um laço de repetição simples com WHILE
c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM!!')


# exemplo 3
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM')


# Exemplo 4 (o programa somente será interompido quando o valor for 0)
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('Fim do Programa!!')

# Exemplo 5
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um numero: '))

    # O programa irá tratar o 0 com par, iremos evitar isso com essa condicional
    if n != 0:
        if n % 2 == 0:
            par = par + 1

        else:
            impar = impar + 1

print('Você digitou {} numeros pares e {} numeros ímpares!'.format(par, impar))

