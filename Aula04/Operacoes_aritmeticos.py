"""
Operações aritméticas
(+) --> Adição
(-) --> Subtração
(*) --> Multiplicação
(/) --> Divisão
(**) --> Exponenciação/potenciação ou pow(,)
(//) --> Divisão inteira
(%) --> Resto da divisão/Módulo
pow(n, (1/2)) --> Calculando a raiz quadrada

1 --> A ordem de precedência sempre será: realizar as operações que estiverem entre (parenteses)
2 --> Em seguida resolve-se a potência **
3 --> logo após vem; *, /, // e %
4 --> E por ultimo são + e -
"""

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
adi = n1 + n2
mul = n1 * n2
div = n1 / n2
sub = n1 - n2

print('A soma entre {} e {} é igual a {}'.format(n1, n2, adi))
print('===============================')
print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, mul))
print('===============================')
print('A divisão entre {} e {} é igual a {}'.format(n1, n2, div))
print('===============================')
print('A subtração entre {} e {} é igual a {}'.format(n1, n2, sub))

""" 
Exemplos de Operações que eu ainda não tinha visto
"""

# Raiz quadrada de um número
a = 81
b = 1 / 2
c = a ** b
print(c)
print('=' * 20)

# Descobrindo a raiz cúbica de um número
a = 127
b = 1 / 3
c = a ** b
print(c)
print('=' * 20)


# Trabalhando com strings
print('a' + 'olá')
print('=' * 20)
print('oi' * 5)
print('=' * 20)

# Formatando a saida de uma string de formas diferentes
nome = input('Qual é o seu nome? ')
print('Olá {}, seja bem vindo ao Python!!'.format(nome))  # Formatação normal
print('=' * 20)  # Apenas para dar espaços entre um print e outro

# Adicionando caracteres á direita do nome
print('Olá {:<20}, seja bem vindo ao Python!!'.format(nome))
print('=' * 20)

# Adcionando caracteres á esquerda do nome
print('Olá {:>20}, seja bem vindo ao Python!!'.format(nome))
print('=' * 20)

# Centralizando o nome
print('Olá {:^20}, seja bem vindo ao Python!!'.format(nome))
print('=' * 20)

# Centralizando o nome e o colocando entre símbolos
print('Olá {:=^20}, seja bem vindo ao Python!!'.format(nome))


""" Lendo dois numeros inteiros e formatando com varias operações """
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

soma = num1 + num2
mult = num1 * num2
divi = num1 / num2
Dint = num1 // num2
expo = num1 ** num2

p
rint('A soma é {}, a multiplicação é {} e a divisão é {}'.format(soma, mult, divi))
print('='*20)
print('A divisão inteira é {} e a exponenciação é {}'.format(Dint, expo))
print('=' * 20)

"""
Obs: quando o resultado de qualquer operação tiver várias casas decimais,
é posivel utilizar a formtação{:.3f} para especificar que queremos
apenas 03 casas decimais por exemplo. Veja a saída formatada abaixo"""
print('A divisão com 3 casas decimais é {:.3f}'.format(divi))

# Se quisermos concatenar dois prints em uma mesma linha, é so adicionar ", end='' (Dentro
# da aspas simples você pode colocar algum caracter para diferenciar um print do outro
