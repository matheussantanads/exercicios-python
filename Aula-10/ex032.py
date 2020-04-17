# Curso Python 10
# ---Desafio 32---
# Faça um programa que leia um ano qualquer e 
# mostre se ele é bissexto.

ano = int(input('Digite um ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 4 == 0 and ano % 400 == 0 or ano % 4 != 0 and ano % 400 == 0:
    print('é bissexto')
else:
    print('não é bissexto')
