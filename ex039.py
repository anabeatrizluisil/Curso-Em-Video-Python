# Desafio 39 - Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
ano = int(input('Digite o ano em que você nasceu: '))
idade = datetime.date.today().year - ano

if idade > 18:
    print('Já passou da hora de se alistar. Você está {} anos atrasado.'.format(idade - 18))
elif idade < 18:
    print('Ainda não é hora de se alistar. Faltam {} anos.'.format(18 - idade))
else:
    print('É a hora de se alistar!')

