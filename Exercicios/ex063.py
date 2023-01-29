# Desafio 63 - Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência Fibonacci

# Fn = Fn-1 + Fn-2

primeiro = 0
segundo = 1

n_termos = int(input('Quantos elementos da sequência de fibonnaci você quer ver?'))

c = 1
while c < n_termos + 1:
    if c == 1:
        termo = 0
        print('{} -> '.format(termo), end='')
    elif c == 2:
        termo = 1
        print('{} -> '.format(termo), end='')
    else:
        termo = primeiro + segundo
        print('{} -> '.format(termo), end= '')
        primeiro = segundo
        segundo = termo
    c += 1
print('FIM')
