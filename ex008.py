# Desafio 08 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metro = float(input('Digite um valor em metros: '))

cm = metro * 100
mm = metro * 1000

print('Conversão em cm: {:.1f}'.format(cm))
print('Conversão em mm: {:.1f}'.format(mm))
