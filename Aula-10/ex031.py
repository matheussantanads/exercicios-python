# Curso Python 10
# ---Desafio 31---
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule 
# o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
# $0,45 parta viagens mais longas.

dist = float(input('Qual a distância da viagem? '))
if dist <= 200:
    print(f'Para a viagem de {dist}km o preço da passagem é de R${dist*0.5:.2f}')
else:
    print(f'Para a viagem de {dist}km o preço da passagem é de R${dist*0.45:.2f}')
