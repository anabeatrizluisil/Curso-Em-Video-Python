# Desafio 31 - Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
# cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

km = float(input('Vamos calcular o preço da passagem. Digite quantos km a viagem terá: '))

if km >= 200:
    passagem = km * 0.45
else:
    passagem = km * 0.50

print("O preço da passagem é R${:.2f}".format(passagem))