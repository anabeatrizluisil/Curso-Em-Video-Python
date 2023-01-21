# Desafio 18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math

angulo = float(input('Digite o ângulo a ser digitado: '))

ang_graus = math.radians(angulo)

print('O seno de {} é {:.2f}'.format(angulo, math.sin(ang_graus)))
print('O cosseno de {} é {:.2f}'.format(angulo, math.cos(ang_graus)))
print('A tangente de {} é {:.2f}'.format(angulo, math.tan(ang_graus)))
