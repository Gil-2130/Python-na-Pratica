"""

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

"""

# solicitando a frase
frase = str(input('Digite uma frase: ')).strip().upper()

# Dividindo o texto (O resultado será uma lista de palavras)
palavras = frase.split()

# Unindo todas as palavras dentro da lista com o join
uniao = ''.join(palavras)

# armazenando o texo invertido em uma variavel
inverso = ''

# laço para realizar a inversão do texto
for letra in range(len(uniao) - 1, -1, -1):

    # Adicionando o resultado do laço á variavel
    inverso += uniao[letra]

# Imprimindo a frase original e o resultado da inversão
print('O inverso de "{}" é "{}"'.format(frase, inverso))

# Condicional para saber se o texto é palíndromo
if inverso == uniao:
    print('A frase é um palíndromo!')

# Senão...
else:
    print('O texto não é um palíndromo!!')


#  SIMPLIFICANDO
# solicitando a frase
frase = str(input('Digite uma frase: ')).strip().upper()

# Dividindo o texto (O resultado será uma lista de palavras)
palavras = frase.split()

# Unindo todas as palavras dentro da lista com o join
uniao = ''.join(palavras)

# armazenando o texo invertido em uma variavel
inverso = uniao[::-1]

# Imprimindo a frase original e o resultado da inversão
print('O inverso de "{}" é "{}"'.format(frase, inverso))

# Condicional para saber se o texto é palíndromo
if inverso == uniao:
    print('A frase é um palíndromo!')

# Senão...
else:
    print('O texto não é um palíndromo!!')
