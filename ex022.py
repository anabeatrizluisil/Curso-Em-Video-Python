# Desafio 22 - Crie um programa que leia o nome completo de uma pessoa e mostra:
# - O nome com todas as letras maíusculas
# - O nome com todas minúsculas
# - Quantas letras ao total (sem considerar espaços)
# - Quantas letras tem o primeiro nome

nome = str(input("Digite o seu nome completo: ")).strip()

qtd_letras = len(nome) - nome.count(' ')

lista_nome = nome.split()


print("Todas as letras maiúsculas: {}".format(nome.upper()))
print("Todas as letras minúsculas: {}".format(nome.lower()))
print("Quantidade de letras (ignorando espaços): {}".format(qtd_letras))
print("Quantidade de letras do primeiro nome: {}".format(len(lista_nome[0])))


