# Curso Python 13
# ---Desafio 56---
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do 
# programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho 
# e quantas mulheres têm menos de 20 anos.

idadeT = int(0)
ma = int(0)
count = int(0)

for c in range(0, 4):

    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo F/M: ')).strip().upper()

    if sexo == 'M':
        if idade > ma:
            ma = idade
            maisvelho = str(nome)
    else:
        if idade < 20:
            count += 1

    print('\n')
    idadeT += idade

print(f'A média de idade do grupo é {idadeT/4:.1f} anos')
print(f'O homem mais velho é {maisvelho}')
print(f'{count} mulheres tem menos de 20 anos')
