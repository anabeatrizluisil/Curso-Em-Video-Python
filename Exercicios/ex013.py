# Desafio 13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Qual é seu salário? '))

aumento = salario + (salario * (15/100))

print('Seu novo salário com 15% de aumento é {}'.format(aumento))