# Curso Python 09
# ---Desafio 26---
# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes
# aparece a letra A. Em que posição ela aparece a primeira vez. Em que 
# posição ela aparece a última vez

frase = str(input('Digite algo: ')).strip()

print('a letra A se repete {}'.format(frase.upper().count('A')))
print('Ela aparece a primeira vez na posição {}'.format(frase.upper().find('A')+1))
print('Ela aparece a ultima vez na posição {}'.format(frase.upper().rfind('A')+1))
