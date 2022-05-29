# Estrutura de repetição finita (Ela para quando a flag for falsa)
cont = 1

# Enquanto o contador for menor ou igual a 10
while cont <= 10:
    print(cont, '-> ', end='')
    cont = cont + 1
print('FIM')

# Estrutura de repetição infinita (Cuidado ao executar o código pois o PC pode travar)
# cont = 1
# while True:
#     print(cont, '-> ', end='')
#     cont = cont + 1
# print('FIM')

# Exemplo 3
# Variavel que armazena o input
n = 0

# Contador do input
cont = 0
while n < 15:
    n = int(input('Digite um número: '))
    cont = n + 1
print(cont)

# Exemplo 4
n = 0
soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    soma = soma + n
print(f'A soma vale {soma}')
# Note que no final, a flag também foi somada, e não é isso que queremos


# Exemplo 5
n = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 100:
        break
    soma = soma + n

print(f'A soma vale {soma}')
# Observe que a flag no "if" não foi somada. Essa é a forma correta de se interromper um laço
