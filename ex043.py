# Desafio 43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5 : Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 a 30: Sobrepeso
# - 30 até 40: obesidade
# - Acima de 40: obesidade mórbida

altura = float(input('Digite sua altura (m): '))
peso = float(input('Digite seu peso (kg): '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é {:.2f}. Categoria: abaixo do peso.'.format(imc))
elif imc >= 18.25 and imc < 25:
    print('Seu IMC é {:.2f}. Categoria: peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f}. Categoria: sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.2f}. Categoria: obesidade.'.format(imc))
elif imc < 40:
    print('Seu IMC é {:2f}. Categoria: obesidade mórbida.'.format(imc))