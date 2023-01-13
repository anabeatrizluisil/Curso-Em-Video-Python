# Desafio 34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário em R$: '))

if salario > 1250:
    aumento = 0.10
else:
    aumento = 0.15

novo_salario = salario + (aumento * salario)

print('Seu novo salario é de R${}'.format(novo_salario))