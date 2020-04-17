# Curso Python 12
# ---Desafio 41---
# A Confederação Nacional de Natação precisa de um programa 
# que leia o ano de nascimento de um atleta e mostre sua 
# categoria, de acordo com a idade

from datetime import datetime

ano = int(input('Em que ano você nasceu? '))
idade = datetime.today().year-ano

print(f'Sua idade é {idade} anos')

if idade < 9:
    print('Categoria: Mirim')
elif 9 <= idade < 14:
    print('Categoria: Infantil')
elif 14 <= idade < 19:
    print('Categoria: Júnior')
elif 19 <= idade < 25:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')
