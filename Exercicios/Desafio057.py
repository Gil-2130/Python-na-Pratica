"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.

Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

# Variável com os sexos
sexo = 'M', 'F'


while sexo != 'M' or sexo != 'F':
# ou
# while sexo not in 'MmFf'

    # SOLICITANDO O SEXO da pessoa
    sexo = str(input('Qual o seu sexo?\n'
                     '[M/F]: ')).strip().upper()

    # Se o sexo for masculino
    if sexo == 'M':
        print('Seu sexo é masculino')

    # Se o sexo for feminino
    elif sexo == 'F':
        print('Seu sexo é feminino.')

    #
    else:
        print('Opção inválida!!!')

        # utilizei o break para interromper o codigo quando a opção foi inválida
        # Não é obrigatório
        break


# REsposta do Professor

# Solicitando o sexo
sexo = str(input('Informe o seu sexo:\n'
                 '[M/F] ')).strip().upper()[0] # strip e upper removem espaços e coloca
                                            # a resposta em letra maiúscula

# Enquanto o input não estiver denro dos dados esperados
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos! Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado!'.format(sexo))
