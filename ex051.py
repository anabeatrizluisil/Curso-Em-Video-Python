# Desafio 51 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa regressão.

primeiro = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão da PA: '))

# An = A1 + (n-1) * r

for c in range(1, 11):
    termo = primeiro + ((c - 1) * razao)
    print('Termo {}: {}'.format(c, termo))
