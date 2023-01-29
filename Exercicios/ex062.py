# Desafio 62 - Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

# An = primeiro + (n-1) * r

c = 1

while c < 11:
    termo = primeiro + (c - 1) * razao
    print('Termo {}: {}'.format(c, termo))
    c += 1

novos_termos = int(input('Quantos termos você quer mostrar a mais? '))

c_novo = 11

iteracao = 11 + novos_termos
while novos_termos != 0:

    while c_novo < (iteracao):
        termo_novo = primeiro + (c_novo - 1) * razao
        print('Termo {}: {}'.format(c_novo, termo_novo))
        c_novo += 1

    novos_termos = int(input('Quantos termos você quer mostrar a mais? '))
    iteracao = iteracao + novos_termos

print('Finalizando...')