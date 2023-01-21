# Desafio 38 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma imagem
# o primeiro valor é maior
# o segundo valor é maior
# não existe valor maior, os dois são iguais

num1 = float(input('Digite um número qualquer: '))
num2 = float(input('Digite outro número qualquer: '))

if num1 > num2:
    print('O primeiro valor é maior.')
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais.')
else:
    print('O segundo valor é maior.')