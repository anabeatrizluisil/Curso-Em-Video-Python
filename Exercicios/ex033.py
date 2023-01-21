# Desafio 33 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um segundo número: '))
n3 = float(input('Digite um terceiro número: '))

print('O maior desses números é: {}'.format(max(n1, n2, n3)))
print('O menor desses números é: {}'.format(min(n1, n2, n3)))

