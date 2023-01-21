# Desafio 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# Considere 1 dólar = 3.27 reais

dinheiro = float(input('Digite quanto você tem na carteira: R$'))

dolar = dinheiro / 3.27

print('Você pode comprar USD {:.2f} dólares'.format(dolar))