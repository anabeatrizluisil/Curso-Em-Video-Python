# Desafio 53 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase para verificar se ela é palindromo: ')).strip().replace(' ', '').upper()

metade = int((len(frase) - 1) / 2)

soma = 0
for c in range(1, metade + 1):
    if frase[c-1] == frase[-c]:
        soma += 1

if soma == metade:
    print('Essa palavra é um palíndromo!')
else:
    print('Essa palavra não é um palíndromo!')