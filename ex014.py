# Desafio 14 - Escreva um programa que converta uma temperatura digitada em C e converta para F

celsius = float(input('Informe a temperatura em °C: '))

frhnt = (celsius * 1.8) + 32

print('A temperatura de {}°C corresponde a {:.1f}°F'.format(celsius, frhnt))

