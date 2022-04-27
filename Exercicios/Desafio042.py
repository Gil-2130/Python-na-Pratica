"""
REfaça o desafio035 dos triangulos, acrescentando o recurso de mostrar
que tipo de triangulo será formado

 - EQUILATERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais
 - ESCALENO: Todos os lados diferentes
"""

# Obtendo as medidas
a = 5
b = 10
c = 9

# condição para formar o triãngulo
tri = a < b + c and b < c + a and c < b + a
print(tri)  # A saída será True pois os valores atendem á formula

# Obtendo o tamanho dos lados do possível triângulo
a1 = float(input('Digite o tamanho do lado A: '))
b1 = float(input('Digite o tamanho do lado B: '))
c1 = float(input('Digite o tamanho do lado C: '))

# Condicional para a formação de um triangulo
if a1 < b1 + c1 and b1 < a1 + c1 and c1 < a1 + b1:
    
    # Condicional para verificar que tipo de triangulo será criado
    if a1 == b1 and a1 == c1 and b1 == c1:
        print('O triangulo é um EQUILÁTERO!')
    elif a1 == b1 or a1 == c1 or b1 == c1:
        print('O triangulo é um ISÓSCELES!')
    elif a1 != b1 and a1 != c1 and b1 != c1:
        print('O triângulo é um ESCALENO!')
      
    print('Sim, é possível formar um triângulo com os valores informados!')

else:
    print('Não, não é possível formar um triangulo com os valores informados!')
