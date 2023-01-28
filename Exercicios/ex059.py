# Desaio 59 - crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# Seu programa deverá realizar a operação em cada caso

from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

opcao = 0

while opcao != 5:
    print('MENU')
    print('[1] - somar')
    print('[2] - multiplicar')
    print('[3] - maior')
    print('[4] - novos números')
    print('[5] - sair do programa')

    opcao = int(input('>>> Qual é sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma é {}.'.format(soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicação é {}.'.format(multiplicacao))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número é {}.'.format(maior))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa.')
    else:
        print('Opção inválida. Tente novamente.')

    sleep(1)

