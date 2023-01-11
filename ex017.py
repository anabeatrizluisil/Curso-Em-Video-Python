# Desafio 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triÂngulo retângulo
# e calcule e mostre o comprimento da hipotenusa
import math

cateto_op = float(input('Digite o valor do cateto oposto: '))
cateto_adj = float(input('Digite o valor do cateto adjacente: '))

hipot = math.hypot(cateto_op, cateto_adj)

print('A hipotenusa do triângulo é {:.2f}'.format(hipot))
