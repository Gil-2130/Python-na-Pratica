"""
Desenvolva um programa que leia o comprimento de 03 retas e diga ao usuario
se elas podem ou não formar um triangulo
"""

# Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
# um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados
# e menor que a soma dos outros dois lados. Veja o resumo da regra abaixo:
# Exemplo da fórmula de como criar um triangulo
a = 5
b = 10
c = 9

tri = a < b + c and b < c + a and c < b + a
print(tri)  # A saída será True pois os valores atendem á formula

# A minha Solução
a1 = float(input('Digite o tamanho do lado A: '))
b1 = float(input('Digite o tamanho do lado B: '))
c1 = float(input('Digite o tamanho do lado C: '))

if a1 < b1 + c1 and b1 < a1 + c1 and c1 < a1 + b1:
    print('Sim, é possível formar um triângulo com os valores informados!')
else:
    print('Não, não é possível formar um triangulo com os valores informados!')
