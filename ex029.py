# Desafio 29 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite

vel = float(input('Digite a velocidade do carro (em km/h): '))

if vel > 80.0:
    multa = (vel - 80) * 7
    print("Você ultrapassou a velocidade permitida. Sua multa será de R${:.2f}".format(multa))

print("Dirija com segurança!")