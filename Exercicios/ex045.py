# Desafio 45 - Crie um programa que faça o computador jogar jokempo com você

from random import choice

computador = choice(['Pedra', 'Papel', 'Tesoura'])

print('Vamos jogar Pedra, Papel e Tesoura...')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
jogador = int(input('Sua opção: '))

if jogador == 1:
    jogador = 'Pedra'
elif jogador == 2:
    jogador = 'Papel'
elif jogador == 3:
    jogador = 'Tesoura'
else:
    print('Número inválido, tente novamente.')


if computador == jogador:
    print('Você jogou {} e o computador jogou {}. \033[33mEMPATE!'.format(jogador, computador))
elif (computador == 'Pedra' and jogador == 'Tesoura') or (computador == 'Papel' and jogador == 'Pedra') or (computador == 'Tesoura' and jogador == 'Papel'):
    print('Você jogou {} e o computador jogou {}. \033[31mVOCÊ PERDEU!'.format(jogador, computador))
elif (computador == 'Pedra' and jogador == 'Papel') or (computador == 'Papel' and jogador == 'Tesoura') or (computador == 'Tesoura' and jogador == 'Pedra'):
    print('Você jogou {} e o computador jogou {}. \033[32mVOCÊ GANHOU!'.format(jogador, computador))
else:
    print('Combinação desconhecida. Tente novamente.')


