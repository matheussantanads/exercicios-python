# Curso Python 13
# ---Desafio 52---
# Faça um programa que leia um número inteiro 
# e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
s = int(0)

for c in range(1, n + 1):
    a = n / c
    b = int(a)
    if n / c != 1 or n / c != n:
        if a == b:  # Se a divisão entre a e c for inteira
            s += 1  # conta quantas divisões inteiras existem
if s > 2:
    print(f'{n} tem {s} divisores, ele \033[31mnão é primo\033[m')
else:
    print(f'{n} só pode ser dividido por 1 ou ele mesmo, ele \033[32mé primo\033[m')
