# Curso Python 09
# ---Desafio 22---
# Crie um programa que leia o nome completo de uma pessoa e mostre: O nome
# com todas as letras maiuscúlas, O nome com toso minúsculas, Quantas letras
# ao todo sem considerar espaços, Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome: ')).strip()

print(f'Maiúsculo: {nome.upper()}')
print(f'Minúsculo: {nome.lower()}')

div = nome.split(' ')
sepCount = len(div)-1

print(f'Seu nome possui {len(nome)-sepCount} letras')
print(f'Seu primero nome tem {len(div[0])} letras')
