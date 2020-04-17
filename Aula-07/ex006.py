# Curso Python 07
# ---Desafio 06---
# Crie um algoritmo que leia um número 
# e mostre o seu dobro, triplo e raiz quadrada. 
# SEM USAR A BIBLIOTECA MATH

n = int(input('Digite um número: '))

print('{:=^65}'.format(' Resultado '))
print(f'{2*n} é o dobro de {n}, {3*n} é seu triplo e {n**0.5:.2f} é sua raiz quadrada.')
