# Desafio 68 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que
# ele conquistou no final do jogo.
from random import randint

print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)

cont = 0

while True:
    computador = randint(0, 10)
    num = int(input('Diga um valor: '))

    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]

    print('-'*50)
    soma = num + computador

    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'

    print(f'Você jogou {num} e o computador {computador}. Total de {soma}. DEU {resultado}')
    print('-'*50)
    if resultado[0] != escolha:
        print('Você PERDEU')
        break
    elif resultado[0] == escolha:
        print('Você GANHOU')
        cont += 1

print(f'GAME OVER! Você venceu {cont} vezes.')

