# Curso Python 08
# ---Desafio 18---
# Faça um programa que leia um ângulo qualquer e mostre 
# na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians

ang = float(input('Digite o ângulo: '))

print(f'O seno de {ang}º vale {sin(radians(ang)):.2f}')
print(f'O cosseno de {ang}º vale {cos(radians(ang)):.2f}')
print(f'A tangente de {ang}º vale {tan(radians(ang)):.2f}')
