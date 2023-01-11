from math import sqrt, floor
import random
import emoji


num = int(input('Digite um número: '))

raiz = sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

num1 = random.randint(1, 10)
print(num1)

print(emoji.emojize('Olá, mundo :earth_americas:', language = 'alias'))




