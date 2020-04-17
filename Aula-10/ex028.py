# Curso Python 10
# ---Desafio 28---
# Escreva um programa que faça o computador "pensar" em um número inteiro entre
# 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
# computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente advinhar... ')
print('-=-'*20)

n = int(random.randint(0, 5))
num = int(input('Qual número eu pensei? '))

if num==n:
    print('Acertô mizerávi!')
else:
    print('ERRRROOUUU')

print(f'O número era {n}')
