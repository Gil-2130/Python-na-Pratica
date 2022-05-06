"""
Crie um programa que tenha uma tupla com várias palavras(Não use acentos).
Depois disso, você deve mostrar, para cada palavra
quais são as suas vogais.

"""
# Criando a tupla de palavras
palavras = ('maria', 'jose', 'pedro', 'macarrao')


# Realizando um laço nas palavras da tupla
for palavra in palavras:
    # Imprimindo as palavras
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ')
    
    # laço de letras nas palavras
    for letra in palavra:
    
        # Condicional para buscar apenas as letras
        if letra.lower() in 'aeiou':
            print(letra.upper())
    
        # Este else é opcional, pois queremos apenas as vogais.
        else:
            print('Esta não é uma vogal...')
