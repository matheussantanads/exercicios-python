# Curso Python 13
# ---Desafio 49---
# Refaça o Desafio 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Deseja ver a tabuada de qual número? '))

for c in range(0, 11):
    print(f'{n} x {c} = {n*c}')
