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
    print('Seu IMC é {:.1f}'.format(imc))
    print('Alimente-se, você está abaixo do peso!')

elif 18.5 <= imc < 25:
    print('Seum IMC é {:.1f}'.format(imc))
    print('Muito bem! você está no peso ideal.')

elif 25 <= imc < 30:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Fique atento, você está cima do peso')

elif 30 <= imc < 40:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Alerta! você está obeso.')

elif imc >= 40:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Sugiro entrar em uma programa para tratar a obesidade!')
