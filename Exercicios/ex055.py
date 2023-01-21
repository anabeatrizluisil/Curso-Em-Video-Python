# Desafio 55 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o peso maior e o menor.

peso_lista = []

for c in range(0, 5):
    peso = float(input('Digite seu peso (kg): '))
    peso_lista += [peso]

print('O maior peso é {} kg.'.format(max(peso_lista)))
print('O menor peso é {} kg'.format(min(peso_lista)))