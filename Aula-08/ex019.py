# Curso Python 08
# ---Desafio 19---
# Um professor quer sortear um dos seus quatro alunos para apagar o 
# quadro. Faça um programa que ajude ele, lendo o nome dos alunos e 
# escrevendo na tela o nome do escolhido.

from random import choice

n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
alunos = [n1, n2, n3, n4]
esc = choice(alunos)

print(f'O escolhido foi {esc}')
