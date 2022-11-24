"""
  Nessa aula iremos trabalhar com tipos primitivos na prática;
    Em Python existem 04 tipos primitivos; int, float, bool e str.
    int = numeros inteiros
    float = numeros flutuantes(com casas decimais)
    bool = True ou False
    str = string, texto, numeros e simbolos dentro de aspas simples ou duplas
  
"""

# vejamos o exemlpo abaixo:
n1 = input('Digite um numero: ')
n2 = input('Digite outro numero: ')
s = n1 + n2

print('A soma vale', s)
print('===========================')
print('A soma agora vale {}'.format(s))
print('===========================')

"""
Perceba que a saída acima foi bem diferente do que imáginavamos certo?
isso porque o input sempre irá receber strings como argumento.

Então nosso trabalho é convereter essa saída em numero int ou float.

Vejamos a resolução;
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
print('A soma é:',s)
print('===========================')
print('A soma entre', n1, 'e', n2, 'é', s)
print('===========================')
print(f'A soma entre {n1} e {n2}, é {s}')
print('===========================')
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))

"""Obs; coloquei vários prints para formatar de várias formas as saídas"""

# Viu a diferença?

# Para verificar o tipo de dado de uma variavel;
print(type(s))

# Tipos booleanos
n1 = bool(input('Digite'))
print(n1)  # A saída será um True ou False dependendo da entrada

# É um número? (ou é possivel converter a entrada para um número?)
n1 = input('Digite: ')
print(n1.isnumeric())

# É alfa? ( Alfabetico, letras, palavras?
n1 = input('Digite qualque coisa: ')
print(n1.isalpha())

# É Alfa numérico? (combinaçoes de letras e numeros)
n1 = input('Digite qualquer coisa: ')
print(n1.isalnum())

# Tudo que executamos acima foram os tipos.


