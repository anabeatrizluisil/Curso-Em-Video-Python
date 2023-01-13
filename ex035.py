# Desafio 35 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

print('Vamos verificar se 3 retas podem formar um triângulo!')
a = float(input('Digite o valor da reta 1: '))
b = float(input('Digite o valor da reta 2: '))
c = float(input('Digite o valor da reta 3: '))

if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar um triângulo.')