# Desafio 54 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da pessoa {}: '.format(c)))
    idade = datetime.date.today().year - ano

    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('Existem {} pessoas maiores de 21 anos e {} pessoas menores.'.format(maior, menor))