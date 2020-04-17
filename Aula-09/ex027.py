# Curso Python 09
# ---Desafio 27---
# Faça um programa que leia o nome completo de uma pessoa mostrando
# em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome: ')).strip()
div = nome.lower().title().split(' ')

print(f'{div[len(div)-1]}, {div[0]}')
