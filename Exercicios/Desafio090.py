"""
Faça um programa que leia o nome e média do aluno,
guardando também a situação em um dicionário.
No final mostre o conteúdo da estrutura na tela
"""
nome = dict()
media = dict()
situacao = list()

for c in range(0, 1):
    nome = str(input('Nome: '))
    media = float(input(f'Média de {nome}: '))
    print(f'Nome é igual a {nome}')
    print(f'Média é igual a {media}')
    if media >= 7:
        situacao.append(media)
        print(f'O aluno(a) {nome} teve média acima de 7 e está Aprovado!')
    else:
        print(f'O aluno(a) {nome} teve média abaixo de 7 e está Reprovado!')
        
        
        #=============== RESPOSTA DO PROFESSOR ==========#
# Criando um dicionário
aluno = dict()
# Adicionando elementos ao dicionário
aluno['Nome'] = str(input('Digite o seu nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

# Condicional para aprovação
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
# Condicional para recuperação
elif aluno['Média'] >= 5  or aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
# Caso contrário ele estará reprovado
else:
    aluno['Situação'] = 'Reprovado'
# imprimindo organizador
print('-=' * 30)

# Laço para obter os itens do nosso dicionário
for key, value in aluno.items():
    print(f'   - {key} é igual a {value}')
