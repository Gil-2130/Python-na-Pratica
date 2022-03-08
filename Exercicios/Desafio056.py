"""
desenvolva um programa que leia o nome, idade e sexo de 04 pessoas.
No final do programa mostre:
1. A média de idade do grupo.
2. Qual é o nome do homem mais velho
3. Quantas mulheres tem menos de 20 anos
"""

# Salvando a soma da idade
soma_idade = 0

# Salvando a média de idade das pessoas
media_idade = 0

# Salvando a idade e nome do homem mais velho
homem_velho = 0
nome_velho = ''

# Salvando a idade da mulher para fazer a comparação
idade_mulher = 0


# laço de repetição para o input
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))

    # Solicitando nome, idade e sexo da pessoa
    nome = str(input('Nome: ').upper()).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    # Realizando a soma de idades
    soma_idade = soma_idade + idade

    # condicional para sexo masculino
    if p == 1 and sexo in 'Mm':
        homem_velho = idade
        nome_velho = nome

    # Condicional de sexo masculino e homem mais velho
    if sexo in 'Mm' and idade > homem_velho:
        homem_velho = idade
        nome_velho = nome

    # Condicional para mulher abaixo de 20 anos
    if sexo in 'Ff' and idade < 20:
        idade_mulher = idade_mulher + 1

# Calculandoa média de idade do grupo
media_idade = soma_idade / 4

# Imprimindo o resultado formatado
print('A média de idade do grupo é de {} anos.\n'
      'O homem mais velho tem {} anos e se chama {}.\n'
      'Ao todo são {} mulheres abaixo de 20 anos'.format(media_idade,homem_velho, nome_velho, idade_mulher))
