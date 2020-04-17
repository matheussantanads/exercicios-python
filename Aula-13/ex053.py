# Curso Python 13
# ---Desafio 53---
# Crie um programa que leia uma frase qualquer e diga
# se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')

print(f'Você digitou {frase}')

s = int(0)

for c in range(len(frase), 0 , -1):
    if frase[c-1] == frase[len(frase)-c]:
        s += 1

if s == len(frase):
    print(f'{frase} É um palíndromo')
else:
    print(f'{frase} Não é um palíndromo')
