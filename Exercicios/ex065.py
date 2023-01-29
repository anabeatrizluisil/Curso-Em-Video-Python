# Desafio 65 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores
# lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

resposta = 'a'
count = 0
soma = 0

maior = menor = 0

while resposta not in 'Nn':

    num = int(input('Digite um número: '))


    if count == 0:
        maior = num
        menor = num
    elif count != 0:
        if num > maior:
            maior = num
        elif num < maior:
            menor = num

    count += 1
    soma += num

    resposta = str(input('Quer continuar? ')).upper().strip()[0]

media = soma / count

print('Você digitou {} números e a média foi {}'.format(count, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
