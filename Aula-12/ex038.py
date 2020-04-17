# Curso Python 12
# ---Desafio 38---
# Escreva um programa que leia dois números inteiros e compare-os. mostrando
# na tela uma mensagem: - O primeiro valor é maior - O segundo valor é
# maior - Não existe valor maior, os dois são iguais

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))

if n1 > n2:
    print(f'{n1}, o primeiro valor digitado é maior que {n2}')
elif n2 > n1:
    print(f'{n2}, o segundo valor digitado é maior que {n1}')
else:
    print(f'{n1} é igual a {n2}')
