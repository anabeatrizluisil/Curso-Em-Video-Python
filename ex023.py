# Desafio 23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

num = str(input("Digite um número: "))

num = '000' + num

print("Unidade: {}".format(num[-1]))
print("Dezena: {}".format(num[-2]))
print("Centena: {}".format(num[-3]))
print("Milhar: {}".format(num[-4]))
