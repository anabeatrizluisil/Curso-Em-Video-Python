# Desafio 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))

area = largura * altura

litros = area / 2

print('Você precisará de {} litros de tinta'.format(litros))