# Desafio 26 - Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece pela ultima vez

frase = str(input('Digite uma frase: ')).strip().upper()

print('A palava "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A posição que a letra aparece pela primeira vez: {}'.format(frase.index('A')+1))
print('A última ocorrência da letra é na posição: {}'.format(frase.rindex('A')+1))
