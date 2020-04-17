# Curso Python 12
# ---Desafio 39---
# Faça um programa que leia o ano de nascimento de um jovem e  informe,  de  acordo  com  a  sua
# idade,  se  ele  ainda  vai  se  alistar  ao  serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento. Seu  programa  também  deverá  mostrar  o  tempo  que
# falta  ou  que  passou  do prazo.

from datetime import datetime

data = int(input('Em que ano você nasceu? '))
anoAtual = datetime.today().year
idade = anoAtual-data

if idade < 18:
    print(f'Você ainda nao está com idade para se alistar, faltam {18-idade} anos')
elif idade == 18:
    print('Hora exata para se alistar')
else:
    print('Perdeu o prazo')
