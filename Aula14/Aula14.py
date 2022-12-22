# Criando uma lista vazia
dados = list()

# Adicionando dados á lista(na ultima posição)
dados.append('BlueShift')
dados.append(2022)

# Imprimindo a lista
print(dados)

# Imprimindo determinadas posições da lista(Por índice)
print(dados[0])
print(dados[1])

# Criando lista vazia e adicionado o fatiamento da lista anterior dentro dela(criando uma cópia)
pessoas = list()
pessoas.append(dados[:])  # sem estes parâmetros, as listas seriam interligadas, não é o que queremos(não neste caso).

# Imprimindo nova lista
print(pessoas)

# Obs.; a nova lista possui apenas um elemento e não dois como a lista anterior

# criando uma lista aninhada (listas dentro de listas)
pessoas_0 = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas_0)

# Imprimindo o indíce 0
print(pessoas_0[0])

# Imprimindo o índice 1 e o índice interno deste elemento
print(pessoas_0[1][1])

# Criando uma lista teste
teste = list()
# Adicionando elementos
teste.append('BlueShift')
teste.append(40)

# Criando uma lista galera
galera = list()
# Adicionando elementos da lista anterior de forma independente
galera.append(teste[:])
# Adicionando novos elementos
teste[0] = 'Maria'
teste[1] = 22
# Adicionando
galera.append(teste[:])
print(galera)

for pessoa_1 in galera:
    print(pessoa_1[1])

# Criando lista e lista temporária
galera0 = list()
dado = list()

# criando um laço
for c in range(0, 3):
    # Adicionando dado Nome
    dado.append(str(input('Nome: ')))
    # Adicionando dado Idade
    dado.append(int(input('Idade: ')))
    # Adicionando os dados da lista anterior(cópia)
    galera0.append(dado[:])
    # Após os dados terem sido copiados, iremos excluí-los
    dado.clear()

# imprimindo os dados de Galera0
print(galera0)
# Variável para contabilizar quantas pessoas são maiores de idade
tot_maior = 0
# Variável para contabilizar quantas pessoas são menores de idade
tot_menor = 0
# Criando um laço para obter apenas as idades
for idade in galera0:
    # Se forem maiores de idade
    if idade[1] >= 18:
        print(f'{idade[0]} é maior de idade')
        # Contabilizando os maiores de idade
        tot_maior = tot_maior + 1

    # Se forem menores de idade
    else:
        print(f'{idade[0]} é menor de idade')
        # Contabilizando os menores de idade
        tot_menor = tot_menor + 1

# Imprimindo os totais
print(f'No total temos {tot_maior} adultos e {tot_menor} menores de idade')
