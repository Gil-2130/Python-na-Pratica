"""
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.

O programa encerra quando ele disser que quer mostrar 0 termos.

"""

# Imprimindo msg de Geração de PA
print('Gerando PA')
print('=-=' * 10)

# Obtendo o primeiro termo
prim = int(input('Primeiro Termo: '))

# Razão da PA
razao = int(input('Razão da PA: '))

# guardando o resultado do input do primeiro termo
termo = prim

# Criando contador
cont = 1

# Imprimindo total de PA's
total = 0

# Armzenando novos termos
mais = 10

# Laço enquanto mais for diferente de 0
while mais != 0:

    # armazendo a variavel responsável por solicitar mais PA's
    total = total + mais

    # Laço
    while cont <= total:
        print('{} ⇒ '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    # Imprimindo uma pausa (Fictícia)
    print('PAUSA')

    # Variavel para solicitar mais termos caso o usuário deseje
    mais = int(input('Quantos termos a mais, você deseja mostrar? '))

print('Progressão finalizada com {} termos!'.format(total))
print('=-=' * 10)

# Imprimindo o fim do programa
print('FIM!!')
