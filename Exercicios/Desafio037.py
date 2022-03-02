"""
Desenvolva um programa que leia um numero inteiro qualquer
e peça para o usuário escolher qual será a base de conversão
1. para Binário
2. Para Octal
3. Para Hexadecimal
"""

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n'
      '[1] Converter para BINÁRIO\n'
      '[2] Converter para OCTAL\n'
      '[3] Converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

# Convertendo o número para BINÁRIO
if opcao == 1:
    bina = bin(num)
    print('O numero {} convertido em BINÁRIOS é {}'.format(num, bina))

# Convertendo para OCTAL
elif opcao == 2:
    octal = oct(num)
    print('O numero {} convertido em OCTAL é {}'.format(num, octal))

# Convertendo para HEXADECIMAL
elif opcao == 3:
    hexa = hex(num)
    print('O número {} convertido em HEXADECIMAL é {}'.format(num, hexa))
else:
    print('Opção inválida!!')

"""
Opcionalmente podemos remover as variaveis que armazenam a conversão dos tipos.
Note que o resultado são uma sequencia de letra e números, porém
os primeiros 02 caracteres podem ser removidos com segurança pois eles representam
apenas o tipo de dado ou seja; se é Binário, Octal ou Hexadecimal.

Use a formatação de fatiamento [2:] para remover os dois primeiros caracteres.

Dessa forma:
"""

# Convertendo o número para BINÁRIO
if opcao == 1:
    bina = bin(num)
    print('O numero {} convertido em BINÁRIOS é {}'.format(num, bina [2:]))

# Convertendo para OCTAL
elif opcao == 2:
    octal = oct(num)
    print('O numero {} convertido em OCTAL é {}'.format(num, octal[2:]))

# Convertendo para HEXADECIMAL
elif opcao == 3:
    hexa = hex(num)
    print('O número {} convertido em HEXADECIMAL é {}'.format(num, hexa[2:]))
else:
    print('Opção inválida!!')
