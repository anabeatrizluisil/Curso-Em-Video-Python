# Desafio 48 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
# de 3 e que se encontram no intervalo de 1 até 500

cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma dos {} números ímpares múltiplos de 3 entre 1 e 500 é: {}'.format(cont, soma))



