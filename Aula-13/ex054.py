# Curso Python 13
# ---Desafio 54---
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores

from datetime import datetime

men = int(0)
mai = men

for c in range(0, 7):
    ano = int(input('Digite o ano que você nasceu: '))
    id = datetime.today().year - ano
    if id < 18:
        men += 1
    else:
        mai += 1

print(f'{men} pessoas ainda não atingiram a maioridade')
print(f'{mai} pessoas atingiram a maioridade')
