# Desafio 42 - Refaça o desafio dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('Vamos verificar se 3 retas podem formar um triângulo e caracterizar o tipo dele.')
a = float(input('Digite o valor da reta 1: '))
b = float(input('Digite o valor da reta 2: '))
c = float(input('Digite o valor da reta 3: '))

if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
    print('Essas retas podem formar um triângulo!')
    if a == b == c:
        print('O triângulo é equilátero.')
    elif a == b or a == c or b == c:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Essas retas não podem formar um triângulo.')