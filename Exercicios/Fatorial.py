"""
Fatorial de 01 número:
Crie um programa que irá receber um numero e imprimr o seu fatorial.

# Méto 5Q's:
Analise criticamente o problema e descubra:
(Tente explicar este problemas para si mesmo em voz alta e peça mais informações ou 
investigue mais até você comreender completamente o problema.)

1. Quais são os dados de entrada necessários?
R: numero

2. O que devo fazer com esses dados?
R: Calcular o fatorial de um numero que for passado para o meu programa,
e exibi-lo na tela.

3. Quais são as restrições deste problema?
R: - O numero deve ser um valor inteiro
   - O numero deve ser um valor positivo
   
4. Qual é o resultado esperado?
R: O valor fatorial do numero sugerido

5. Qual a sequencia de passos a ser feita para chegar ao resultado esperado?
input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
    fatorial = fatorial * numero
print(fatorial
"""

numero = int(input('Digite um numero: '))
if numero > 0:
    fatorial = 1
    for item in range(1, numero + 1):
        fatorial = fatorial * item
    print('O fatorial de {} é: {}'.format(numero, fatorial))
