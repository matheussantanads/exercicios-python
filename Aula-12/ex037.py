# Curso Python 12
# ---Desafio 37---
# Escreva um programa em Python que leia um número inteiro
# qualquer e peça para o usuário escolher qual será a base de 
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))

print('Converter esse número para')
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')

op = int(input('Converter esse número para: '))

if op == 1:
    print(f'{n} em Binário é {bin(n)[2:]}')
elif op ==2:
    print(f'{n} em Octal é {oct(n)[2:]}')
elif op == 3:
    print(f'{n} em Octal é {hex(n)[2:]}')
else:
    print('Opção inválida!')
