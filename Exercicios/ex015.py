# Desafio 15 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia
# e R$ 0.15 por km rodado

dias = int(input('Quantos dias rodados? '))
km = float(input('Quantos km rodados? '))

total = (dias * 60) + (0.15 * km)

print('O total a pagar é de R${:.2f}'.format(total))
