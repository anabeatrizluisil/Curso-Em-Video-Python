# Desafio 46 - Faça um programa que mostre na tela uma contagem regressiva para os estouros de fogos de artifício,
# indo de 10 até 0 com uma pausa de 1 segundo entre eles
import time
import emoji

print('='*20)
print('Iniciando contagem')
print('='*20)

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print(emoji.emojize(':fireworks:')*5)