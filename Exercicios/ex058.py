# Desafio 58 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

n = random.randint(0, 10)

print('-.-' * 20)
print('Vou pensar em um número de 0 a 10.')
print('-.-' * 20)

tentativa = int(input('Tente adivinhar: '))
palpites = 1

while tentativa != n:
    if tentativa > n:
        tentativa = int(input('Menos...Tente novamente: '))
    elif tentativa < n:
        tentativa = int(input('Mais... Tente novamente: '))
    palpites += 1

print('\033[32mACERTOU!\033[m O número que pensei foi {}. Você levou {} tentativas para acertar.'.format(n, palpites))