# Curso Python 13
# ---Desafio 50---
# Desenvolva  um  programa  que  leia  seis  números  inteiros  e
# mostre a soma apenas daqueles que forem pares. Se o valor digitado
# for ímpar, desconsidere-o.

s = int(0)

for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n

print(f'O somatório dos números pares digitados são {s}')
