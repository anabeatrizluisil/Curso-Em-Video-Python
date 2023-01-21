# Desafio 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prod = float(input('Digite o preço de um produto: R$'))

novo_valor = prod - (prod * (5 / 100))

print('O valor com 5% de desconto é: R${:.2f}'.format(novo_valor))