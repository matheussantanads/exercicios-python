# Curso Python 13
# ---Desafio 55---
# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

p = float(input('Digite seu peso: '))
me = ma = p

for c in range(0, 4):
    p = float(input('Digite seu peso: '))
    if p > ma:
        ma = p
    elif p < me:
        me = p

print(f'Maior peso lido foi {ma}Kg')
print(f'Menor peso lido foi {me}Kg')