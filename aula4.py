
# Exemplo 1

# nome = 'Guanabara'
# idade = 25
# peso = 75.8

# print(nome, idade, peso)

# Exemplo 2

# nome = input('Qual é seu nome? ')
# idade = input('Quantos anos você tem? ')
# peso = input('Quanto você pesa? ')

# print(nome, idade, peso)

# Desafio 1 - Crie um script python que leia o nome da pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado

nome = input('Qual é seu nome? ')

print("Olá, " + nome + "! Prazer em te conhecer!")

# Desafio 2 - Crie um script que leia o dia, o mês e o ano de nascimento da pessoa e mostra uma mensagem com a data formatada

dia = input('Dia = ')
mes = input('Mes = ')
ano = input('Ano = ')

print("Você nasceu no dia", dia, "de", mes, "de", ano,". Correto?")

# Desafio 3 - Crie um script python que leia dois números e tente mostrar a soma entre eles

num1 = input("Primeiro número ")
num2 = input("Segundo número ")

print("A soma é " + str(int(num1) + int(num2)))