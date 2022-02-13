"""
Faça um programa que leia a largura e a altura da parede em metros,
 em seguida calcule a sua área e a quantidade de tinta necessária para pintá-la,
 sabendo que cada litro de tinda pinta uma área de 2m²
"""
alt_p = int(input('Medida da altura da parede? '))
lar_p = int(input('Medida da largura da parede? '))
area = alt_p * lar_p
print('A area de pintura é de {} m²\n'.format(area),
      'Serão necessários', area/2, 'Litros de tinta')
