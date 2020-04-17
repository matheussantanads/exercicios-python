# Curso Python 10
# ---Desafio 34---
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor
# do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 
# 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual é o salário do funcionário? '))

if sal > 1250.00:
    print(f'Seu novo salário com aumento de 10% é R${sal*1.10:.2f}')
else:
    print(f'Seu novo salário com aumento de 15% é R${sal*1.15:.2f}')
