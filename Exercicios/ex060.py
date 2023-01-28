# Desafio 60 - Faça um programa que leia um número qualquer e mostre seu fatorial.
# Ex: 5! = 5x4x3x2x1

num = int(input('Digite o número para realizar a fatorial: '))

c = num
resultado = 1

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    resultado = resultado * c
    c -= 1
print(resultado)