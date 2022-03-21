Crie um programa que leia a idade eo sexo de várias pessoas.

A cada pessoa cadastrada, o programa deverá pergntar se o usuário quer
ou não continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos Homens foram cadastrados.
C) Qauntas mulheres tem menos de 20 anos

# REsposta do Professor

# Variavel para armazenar todas as idades(não cumulativo)
tot18 = 0
# Guardando a idade do sexo masculino
totH = 0
# Guardando a idade do sexo Feminino
totM = 0
# Loop infinito enquanto for verdade
while True:
    # Input da idade
    idade = int(input('Digite a sua idade: '))
    
    # Variavel para armazenar o sexo 
    sexo = ' '
    # Enquanto a opção digitada não corresponder ao sexo
    while sexo not in 'MF':
        # input do sexo do usuário
        sexo = str(input('Qual o seu sexo?\n'
                         '[M/F]: ')).strip().upper()[0]
    
    # Condicional de idade igual ou maior de 18
    if idade >= 18:
        # Contador de idade maior de 18
        tot18 = tot18 + 1
        
    # Condicional se o sexo for masculino
    if sexo in 'Mm':
        # Contador o sexo masculino
        totH = totH + 1
    # Condicional se o sexo for feminino
    elif sexo in 'Ff' and idade < 20:
        # Contador do sexo Feminino
        totM = totM + 1
    
    # Deseja continuar o programa?
    resp = ' '
    # Enquanto o usuário desejar a execução do programa
    while resp not in 'SN':
        # Input da opção desejada do usuário
        resp = str(input(' Deseja continuar?\n'
                     '[S/N]: ')).strip().upper()[0]
    
    # Condicional se a resposta for NÂO
    if resp in 'Nn':
        print('Programa encerrado!!')
        # Interrompendo o programa
        break
# Mensagens finais
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} Homens Cadastrados')
print(f'E também temos {totM} mulheres com menos de 20 anos.')
