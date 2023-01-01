"""
       Trabalhando com Dicionários
      
"""

# formas de criar dicionários:
dados_0 = dict()
dados_1 = {}
# Verificando o tipo
print(type(dados_0))
print(type(dados_1))

# trabalhando com dicionários
dados_0 = {'Nome': 'Pedro', 'Idade': 25}
print(dados_0['Nome'])
print(dados_0['Idade'])

# Adicionando elementos a um dicionário
dados_0['Sexo'] = 'M'
print(dados_0['Sexo'])

# Removendo elementos
del dados_0['Idade']
print(dados_0)

# Criando Dicionário Filme
filme = {'Titulo': 'Stars Wars',
         'Ano': 1977,
         'Diretor': 'George Lucas'
         }
# Imprimindo o dicionário
print(filme)

# Imprimindo apenas os valores das chaves no dicionário
print(filme.values())

# Imprimindo apenas as chaves
print(filme.keys())

# Imprimindo os itens do dicionário
print(filme.items())

# Usando o laço for para percorrer um dicionário
for key, value in filme.items():
    print(f'O {key} é {value}.')

# Criando uma lista e adicionando dicionário dentro dela
locadora = list()
filme_0 = {'Filme': ['Stars Wars',
                    'Avengers',
                    'Matrix'],
           'Ano': [1977,
                   2012,
                   1999],
           'Diretor': ['George Lucas',
                       'Joss Whedon',
                       'Wachowski']
           }
print(filme_0)

for key, value in filme_0.items():
    print(f'{key} = {value}')


#===================== PRÁTICA ========================

pessoas = {'Nome': 'Gustavo',
           'Sexo': 'M',
           'Idade': 22}
print(pessoas)
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')

for key, value in pessoas.items():
    print(f'{key} = {value}')

# Nova lista
brasil = []

estado1 = {'UF': 'Rio de Janeiro',
           'Sigla': 'RJ',}
estado2 = {'UF': 'São Paulo',
           'Sigla': 'SP'}

# levando os dicionários para dentro da lista
brasil.append(estado1)
brasil.append(estado2)

# imprimindo a lista "brasil"
print(brasil)
print(brasil[0]['Sigla'])


# laço com dicionários
estado3 = dict()
brasil0 = list()
# Laço para adicionar elementos
for c in range(0, 3):
    # Adicionando UF
    estado3['UF'] = str(input('Unidade Federativa: '))
    # Adicionando Sigla
    estado3['Sigla'] = str(input('Sigla do Estado: '))
    # Aqui precisamos usar o método "COPY" para copiar os elementos(sem repetição)
    brasil0.append(estado3.copy())
print(brasil0)

for estado in brasil0:
    print(estado)

for estado in brasil0:
    for key, value in estado.items():
        print(f'O campo {key} tem valor {value}.')

for estado in brasil0:
    for value in estado.values():
        print(value, end=' ')
    print()
