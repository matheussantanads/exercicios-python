# Curso Python 07
# ---Desafio 15---
# Escreva um programa que pergunte a quantidade de Km percorridos  por um carro 
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço 
# a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))

print(f'O total a pagar é de R$ {60*dias + 0.15*km}')
