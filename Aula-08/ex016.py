# Curso Python 08
# ---Desafio 16---
# Crie um programa que leia um número Real qualquer pelo 
# teclado e mostre na tela a sua porção Inteira.

from math import trunc

n = float(input('Digite um número: '))

print(f'A parte inteira de {n} é {trunc(n)}')
