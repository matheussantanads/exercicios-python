# Curso Python 10
# ---Desafio 29---
# Escreva um programa que leia a velocidade de um carro. Se ele
# ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Velocidade: '))
if vel >80:
    print(f'Você foi multado em R${(vel-80)*7} por exceder a velocidade máxima de 80km/h')

print(f'Velocidade medida {vel}Km/h')
