for c in range(1,6):
    print('Oi')
print('FIM')

for c in range(6, 0, -1):
    print(c)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}.'.format(s))
