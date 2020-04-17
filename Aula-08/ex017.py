# Curso Python 08
# ---Desafio 17---
# Faça um programa que leia o comprimento do cateto 
# oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

from math import sqrt

catO = float(input('Cateto oposto: '))
catA = float(input('Cateto adjacente: '))

print(f'Hipotenusa {sqrt(catO**2+catA**2):.2f}')
