# Desafio 67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado do usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))

    if numero < 0:
        break

    print('-'*35)
    for i in range(1, 11):
        print(f'{numero} x {i:^2} = {numero*i}')
    print('-'*35)

print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')