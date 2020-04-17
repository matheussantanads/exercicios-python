# Curso Python 06
# ---Desafio 04---
# Faça um programa que leia algo pelo teclado 
# e mostre na tela o seu tipo primitivo e todas 
# as informações possíveis sobre ele.

algo = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {algo.__class__}')
print(f'É numérico? {algo.isnumeric()}')
print(f'É alfa? {algo.isalpha()}')
print(f'É alfa-numérico? {algo.isalnum()}')
print(f'É maiúsculo? {algo.isupper()}')
print(f'É minúsculo? {algo.islower()}')
print(f'É captalizado? {algo.istitle()}')
