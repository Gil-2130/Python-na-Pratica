"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa,
calcule seu IMC e mostre seu staus de acordo coma atabela abixo:

 - Abaixo de 18,5 : Abaixo do peso
 - Enre 18,5 e 25 : Peso ideal
 - entre 25 a 30 : Sobrepeso
 - entre 30 e 40 : Obesidade
 - Acima de 40 : Obesidade mórbida
"""

peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura**2)

if imc < 18.5:
    print('Alimente-se, você está abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Muito bem! você está no peso ideal.')
elif imc >= 25 and imc <= 30:
    print('Fique atento, você está cima do peso')
elif imc >= 30 and imc <= 40:
    print('Alerta! você está obeso.')
elif imc >=40:
    print('Sugiro entrar em uma programa para tratar a obesidade!')
