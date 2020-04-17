# Curso Python 07
# ---Desafio 10---
# Crie um programa que leia quanto dinheiro uma pessoa 
# tem na carteira e mostre quantos dólares ela pode comprar. 
# CONSIDERE US$ 1 = R$3,27

val = float(input('Quantos R$ você tem? '))

print(f'Com R$ {val} você pode comprar US$ {val/3.27:.2f}')
