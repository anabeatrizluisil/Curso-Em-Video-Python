# Desafio 27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente

nome_completo = str(input('Digite seu nome completo: ')).strip()

primeiro = nome_completo.split()[0]
ultimo = nome_completo.split()[-1]

print("Primeiro nome: {}".format(primeiro))
print("Ultimo nome: {}".format(ultimo))

