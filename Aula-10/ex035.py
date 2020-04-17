# Curso Python 10
# ---Desafio 35---
# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

from math import fabs

seg1 = float(input('Digite o comprimento do Segmento AB: '))
seg2 = float(input('Digite o comprimento do Segmento BC: '))
seg3 = float(input('Digite o comprimento do Segmento CA: '))

condicao1 = (fabs(seg2 - seg3) < seg1 < (seg2 + seg3))
condicao2 = (fabs(seg1 - seg3) < seg2 < (seg1 + seg3))
condicao3 = (fabs(seg1-seg2) < seg3 < (seg1+seg2))

if condicao1 and condicao2 and condicao3 :
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')
