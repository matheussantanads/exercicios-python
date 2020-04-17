# Curso Python 12
# ---Desafio 42---
# Refaça o Desafio 035 dos triângulos, acrescentando o recurso 
# de mostrar que tipo de triângulo será formado

from math import fabs

seg1 = float(input('Digite o comprimento do Segmento AB: '))
seg2 = float(input('Digite o comprimento do Segmento BC: '))
seg3 = float(input('Digite o comprimento do Segmento CA: '))

condicao1 = (fabs(seg2 - seg3) < seg1 < (seg2 + seg3))
condicao2 = (fabs(seg1 - seg3) < seg2 < (seg1 + seg3))
condicao3 = (fabs(seg1 - seg2) < seg3 < (seg1 + seg2))

if condicao1 and condicao2 and condicao3:
    print('Os segmentos acima podem formar um ', end='')
    if seg1 == seg2 and seg1 == seg3:
        print('Triangulo Equilátero')
    elif seg1 == seg2 or seg2 == seg3 or seg3 == seg1:
        print('Triangulo Isósceles')
    elif seg1 != seg2 and seg2 != seg3:
        print('Triangulo Escaleno')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')
