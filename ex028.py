# Desafio 28 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
from time import sleep

n = random.randint(0,5)

print('-.-' * 20)
print('Vou pensar em um número de 0 a 5.')
print('-.-' * 20)

tentativa = int(input('Digite um número para ver se você adivinha qual é: '))

print('Processando...')
sleep(2)

if n == tentativa:
    print("Certa resposta! Você VENCEU")
else:
    print("Resposta errada. Eu pensei no número {}. Você PERDEU!".format(n))