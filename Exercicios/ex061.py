# Desafio 61 - Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

# An = primeiro + (n-1) * r

c = 1

while c < 11:
    termo = primeiro + (c - 1) * razao
    print('Termo {}: {}'.format(c, termo))
    c += 1