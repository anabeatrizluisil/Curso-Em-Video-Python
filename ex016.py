# Desafio 16 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira
import math

num = float(input('Digite um número: '))

print('O número {} tem a parte inteira {}'.format(num, math.trunc(num)))