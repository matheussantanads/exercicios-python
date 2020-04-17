# Curso Python 09
# ---Desafio 24---
# Crie um programa que leia o nome de uma cidade
# e diga se ela começa com o nome "Santo".

cidade = str(input('Digite o nome da sua cidade: ')).strip().upper()
div = cidade.split(' ')
teste = (div[0] == 'SANTO')

print(f'Começa com Santo? {teste}')
