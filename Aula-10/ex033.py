# Curso Python 10
# ---Desafio 33---
# Faça um programa que leia três números e mostre 
# qual é o maior e qual é o menor.

a = float(input('Digite o numero A: '))
b = float(input('Digite o número B: '))
c = float(input('Digite o número C: '))

me = a
ma = a

if b < a and b < c:
    me = b
if c < a and c < b:
    me = c
if b > a and b > c:
    ma = b
if c > a and c > b:
    ma = c

print(f'{me} é o menor e {ma} é o maior')
