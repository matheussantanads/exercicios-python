# Curso Python 08
# ---Desafio 20---
# O mesmo professor do desafio 019 quer sortear a ordem de apresentação 
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro 
# alunos e mostre a ordem sorteada.

from random import shuffle

alu1 = str(input('Nome do aluno1: '))
alu2 = str(input('Nome do aluno2: '))
alu3 = str(input('Nome do aluno3: '))
alu4 = str(input('Nome do aluno4: '))
alunos = [alu1, alu2, alu3, alu4]
shuffle(alunos)

print(f'Ordem dos alunos é : {alunos}')
