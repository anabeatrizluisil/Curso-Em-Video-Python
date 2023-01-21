# Desafio 37 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
# 1 para binário, 2 para octal, 3 para hexadecimal

num = int(input('Digite um número: '))
conversao = int(input('Digite a base de conversão (1 para binário, 2 para octal e 3 para hexadecimal): '))

if conversao == 1:
    num_bin = bin(num)[2:]
    print('Conversão binária: {}'.format(num_bin))
elif conversao == 2:
    num_oct = oct(num)[2:]
    print('Conversão octal: {}'.format(num_oct))
elif conversao == 3:
    num_hex = hex(num)[2:]
    print('Conversão hexadecimal: {}'.format(num_hex))
else:
    print('Opção inválida. Tente novamente.')
