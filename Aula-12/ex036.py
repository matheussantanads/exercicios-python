# Curso Python 12
# ---Desafio 36---
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

val = float(input('Qual o valor da casa? R$'))
sal = float(input('Quanto é o seu salário? R$'))
ano = int(input('Em quantos anos quer pagar? '))
prest = val/(ano*12)

print(f'Para pagar uma casa de R${val} em {ano} anos a prestação será de R${prest:.2f}.')

if prest > (sal*0.3):
    print('Empréstimo \033[31mNegado\033[m')
else:
    print('Empréstimo \033[32mPermitido\033[m')
