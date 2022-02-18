"""
Crie um programa que leia o nome completo de uma pessoa e mostre;
1. -> O nome com todas as letras maiusculas
2. -> O nome com todas as letras minusculas
3. -> Quantas letras ao todo sem considerar os espaços
4. -> Quantas letras tem o primeiro nome?
"""
nome = input('Qual é o seu nome? ')

# Imprimindo o nome com todas as letras maiusculas
print(nome.upper())

# Imprimindo o nome com todas as letras minusculas
print(nome.lower())

# Contando todas as letras sem contar os espaços
nome_s = nome.split()
nome_s = ''.join(nome_s)
print(len(nome_s))

# Quantas letras tem o primeiro nome?
print(len(nome.split()[0]))