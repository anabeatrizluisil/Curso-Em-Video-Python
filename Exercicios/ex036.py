# Desafio 36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digie seu salário: R$'))
anos = int(input('Em quantos anos você pretende pagar? '))

prestacao = valor_casa / (anos * 12)

print('Valor da prestação: R${:.2f}'.format(prestacao))

if (prestacao) > (salario * 0.3):
    print('Empréstimo negado.')
else:
    print('Empréstimo aprovado.')

