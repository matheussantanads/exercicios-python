# Curso Python 12
# ---Desafio 44---
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento

val = float(input('Digite o valor do produto R$'))

print('[1] à vista dinheiro/cheque: 10% de desconto')
print('[2] à vista no cartão: 5% de desconto')
print('[3] em até 2x no cartão: preço normal')
print('[4] 3x ou mais no cartão: 20% de juros')
      
op = int(input('Escolha uma opção de pagamento: '))

if op == 1:
    print('O valor a ser pago será de R${}'.format(val*0.9))
elif op == 2:
    print('O valor a ser pago será de R${}'.format(val * 0.95))
elif op == 3:
    print('O valor a ser pago será de R${}'.format(val))
elif op == 4:
    print('O valor a ser pago será de R${}'.format(val * 1.2))
else:
    print('\033[31mOpção Inválida\033[m')
