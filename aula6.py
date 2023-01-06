# Desafio 03 - Crie um programa que leia dois números e mostre a soma entre eles

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2

print("A soma é {}".format(s))

# Desafio 04 - Crie um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input("Digite algo: ")

print("Tipo: {}".format(type(algo)))
print("É alfanumérico? {}".format(algo.isalnum()))
print("É numérico? {}".format(algo.isnumeric()))
print("É letra? {}".format(algo.isalpha()))