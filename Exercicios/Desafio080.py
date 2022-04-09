"""
Crie um programa onde o usuário possa digitar 05 valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort())

No final, mostre a lista ordenada na tela.
"""

# Criando uma lista vazia
lista = []

# Laço para obter os inputs do usuário
for c in range(0, 5):
    n = int(input('Digite um valor: '))

    # Por padrão, ao usarmos o append, o número será adicionado ao fim da lista
    # Até que o próximo ocupe o seu lugar.
    if c == 0:
        lista.append(n)

    # Se o input digitado for maior que o último elemento adicionado da lista,
    # Então ele também será adiciondo
    # Pode-se usar     lista[-1]
    elif n > lista[len(lista)-1]:
        lista.append(n)

    # Caso as condiçoes acima não sejam atendidas, faremos outro laço
    # desta vez para verificar se o valor digitado é ao mesmo tempo menor que o ultimo elemento e
    # maior que o primeiro e assim sucessivamente(valor do meio)
    else:
        
        # obtendo posição dos elementos(começando por 0)
        pos = 0
        
        # Varrendo da posição 0 até a última posição
        while pos < len(lista):
        
        # se N for menor que cada elemento da lista
            if n <= lista[pos]:
        
                # Então usamos INSERT para que N assuma a posição do menor elemento da lista
                lista.insert(pos, n)
                
                # Feito isso, damos um break
                break
            
            # Contador da lista, para obter o seu tamanho posteriormnte
            pos = pos + 1

# Imprimindo separador(Para legibilidade do print)
print('-='* 30)

# imprimindo a lista já ordenada
print(f'A lista ordenada é: {lista}')
