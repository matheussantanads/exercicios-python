# Curso Python 09
# ---Desafio 23---
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um 
# dos dígitos separados. Ex 1834 4 unidades 3 dezenas 8 centenas 1 milhar.

n = int(input('Digite um número de 0 a 9999: '))

print(f'Unidade: {n % 10}')
print(f'Dezena: {(n % 100) // 10}')
print(f'Centena: {(n % 1000) // 100}')
print(f'Milhar: {n // 1000}')
