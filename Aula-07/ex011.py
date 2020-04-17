# Curso Python 07
# ---Desafio 11---
# Faça um programa que leia a largura e altura de uma parede em 
# metros, calcule a sua área e a quantidade de tinta necessária para 
# pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

l = float(input('Quanto mede a largura da parede em metros? '))
a = float(input('Quanto mede a altura da parede em metros? '))

print(f'Como a parede tem {l*a:.2f}m² será preciso {(l*a)/2:.2f}L de tinta para pinta-la')
