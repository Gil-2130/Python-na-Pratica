"""
Escreva um programa que ao imiciar, gere um valor aleatório entre 1 e 10
e permita que o usuario chute um numero até que o valor gerado no inicio do
programa seja acertado.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor gerado
no inicio do programa.

# Méto 5Q's:
Analise criticamente o problema e descubra:
(Tente explicar este problemas para si mesmo em voz alta e peça mais informações ou
investigue mais até você comreender completamente o problema.)

1. Quais são os dados de entrada necessários?
R: - valor aleatório de 01 a 10
   - Chute do usuario

2. O que devo fazer com esses dados?
R: Comparar se o chute do usuario foi menor, maior ou igual ao valor
aleatorio de 01 a 10

3. Quais são as restrições deste problema?
R: - Um valor aleatório de 01 a 10

4. Qual é o resultado esperado?
R: O sucesso de acerto do numero aleatório.

5. Qual a sequencia de passos a ser feita para chegar ao resultado esperado?
input valor_aleatorio de 1 a 10
input chute
if chute > valor_aleatorio:
    print 'Chutou alto, tente novamente!
if chute < valor_aleatorio:
    print ' Chutou baixo, tente novamente!'
if chute == valor aleatório
    print 'Você acertou!'
"""

import random

val_rand = random.randint(1, 11)
acertou = False

while acertou == False:
    chute = int(input('Digite um numero de 01 a 10: '))
    if chute < val_rand:
        print('Chute baixo, tente novamente!')
    elif chute > val_rand:
        print('Chute alto, tente novamente!')
    elif chute == val_rand:
        print('Você acertou')
        acertou = True
    else:
        print('Opção inválida')
