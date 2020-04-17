# Curso Python 12
# ---Desafio 45---
# Crie um programa que faça o computador jogar Jokenpô com você.

from emoji import emojize
from random import choice

print('\033[32m-=-\033[m'*10)
print('{:^30}'.format('Jokênpo'))
print('\033[32m-=-\033[m'*10)

opUs = str(input('Pedra, Papel ou Tesoura? ')).strip().lower().capitalize()
op = ['Pedra', 'Papel', 'Tesoura']

if opUs == op[0] or opUs == op[1] or opUs == op[2]:

    opPc = choice(op)
    print(f'Você escolheu {opUs} e o Pc escolheu {opPc}')

    if opUs == op[0]:
        if opPc == op[2]:
            print(emojize('Pc diz: - \033[34mVocê ganhou\033[m :sob:', use_aliases=True))
        elif opPc == op[1]:
            print(emojize('Pc diz: - \033[31mVocê perdeu\033[m :joy:', use_aliases=True))
        else:
            print(emojize('Pc diz: - \033[32mEmpatou\033[m :cry:', use_aliases=True))
    elif opUs == op[1]:
        if opPc == op[0]:
            print(emojize('Pc diz: - \033[34mVocê ganhou\033[m :sob:', use_aliases=True))
        elif opPc == op[2]:
            print(emojize('Pc diz: - \033[31mVocê perdeu\033[m :joy:', use_aliases=True))
        else:
            print(emojize('Pc diz: - \033[32mEmpatou\033[m :cry:', use_aliases=True))
    else:
        if opPc == op[1]:
            print(emojize('Pc diz: - \033[34mVocê ganhou\033[m :sob:', use_aliases=True))
        elif opPc == op[0]:
            print(emojize('Pc diz: - \033[31mVocê perdeu\033[m :joy:', use_aliases=True))
        else:
            print(emojize('Pc diz: - \033[32mEmpatou\033[m :cry:', use_aliases=True))
else:
    print('Pc diz: - Sabe ler? Rode novamente o programa!')
