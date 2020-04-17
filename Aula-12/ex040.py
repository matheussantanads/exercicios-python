# Curso Python 12
# ---Desafio 40---
# Crie um programa que leia duas notas de um aluno 
# e calcule sua média, mostrando uma mensagem no final, 
# de acordo com a média atingida

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
med = (nota1+nota2)/2

if med < 5:
    print('\033[31mReprovado\033[m')
elif 5 <= med <= 6.9:
    print('\033[33mRecuperação\033[m')
else:
    print('\033[34mAprovado\033[m')