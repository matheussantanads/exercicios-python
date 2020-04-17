# Curso Python 09
# ---Desafio 25---
# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome

nome = str(input('Seu nome: ')).strip()
teste = ('SILVA' in nome.upper())
print(f'Tem Silva? {teste}')
