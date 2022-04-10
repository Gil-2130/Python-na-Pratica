"""
Crie um programa onde o usuário digite uma expressão qualquer
e que use parenteses.
O seu programa deverá analisar se a expressão passada
está com os parenteses abertos e fechados na ordem correta
"""

# Exemplo para testar ao nosso programa
# Use (a+b(c+1)*5)) --> use quantos parenteses quiser

# Criando uma variável que armazenará a expressão
expr = str(input(' Digite alguma expressão(por favor use parenteses()): '))

# Criando uma variável para armzanenar os parenteses
pilha = list()

# Criando um laço que irá percorrer a nossa lista
for simb in expr:

    # Condiional para pegarmos parenteses abertos
    if simb == '(':

        # Adicionado o parentese á pilha
        pilha.append('(')

    # Condicional para pegarmos os parenteses fechados
    elif simb == ')':
        # Verificamos se a lista contém elementos, ou seja;
        # AO verificar que há parenteses lá dentro, iremos excluí-lo pois
        # Encontramos o seu par e a expressão se torna válida.
        if len(pilha) > 0:

            # Dropando o último elemento da lista(implicito)
            pilha.pop()

        # Caso contrário, então iremos adicionar este elemento á lista,
        # então saberemos que a expressão se tornará inválida
        else:
            pilha.append(')')
            # Neste momento interrompemos o laço para inserir o elemento apenas uma vez
            break

# Ao final, se o tamanho da nossa pilha for igual a Zero, a expressão será valida
if len(pilha) == 0:
    print('A expressão digitada é válida!')
# Caso contrário, saberemos que a expressão será inválida
else:
    print('A expressão digitada é inválida!!!')
