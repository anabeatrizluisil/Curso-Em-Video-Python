# Desafio 44 - Elabore um programa que calcula o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
# - à vista dinheiro / cheque - 10% desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format('LOJAS GUANABARA'))
preco = float(input('Digite o valor do produto: R$'))
metodo = str(input('Digite A para à vista, B para parcelado ')).upper()

if metodo == 'A':
    tipo = str(input('Digite D para pagamento em dinheiro/cheque ou C para cartão: ')).upper()
    if tipo == 'D':
        desconto = 0.1
    elif tipo == 'C':
        desconto = 0.05
    else:
        print('Tipo errado. Comece novamente.')
elif metodo == 'B':
    vezes = int(input('Em quantas vezes você quer pacelar? '))
    if vezes <= 2:
        desconto = 0
    elif vezes > 3:
        desconto = -0.20
else:
    print('Método inválido. Tente novamente.')

valor_total = preco - (preco * desconto)
print('O valor total da compra é R${:.2f}'.format(valor_total))
