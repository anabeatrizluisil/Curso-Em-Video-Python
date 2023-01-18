# Desafio 41 - A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SENIOR
# - Acima: MASTER
import datetime

ano = int(input('Digite o ano do seu nascimento: '))

idade = datetime.datetime.today().year - ano

if idade <= 9:
    print('Você tem {} anos. Está na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos. Está na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos. Está na categoria JUNIOR'.format(idade))
elif idade <= 20:
    print('Você tem {} anos. Está na categoria SENIOR'.format(idade))
else:
    print('Você tem {} anos. Está na categoria MASTER.'.format(idade))