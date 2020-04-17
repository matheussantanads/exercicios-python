# Curso Python 13
# ---Desafio 51---
# Desenvolva um programa que leia o primeiro termo e 
# a razão de uma PA. No final, mostre os 10 primeiros 
# termos dessa progressão.

t = int(input('Digite o primeiro termo da P.A. :'))
r = int(input('Digite a razão da P.A. (uma constante): '))
pa = t

print(f'a1 = {pa}')

for c in range(1, 10):
    print(f'a{c + 1} = {pa} + {r} = {pa + r}')
    pa += r
