# Curso Python 08
# ---Desafio 21---
# Faça um programa em Python que abra e 
# reproduza o áudio de um arquivo MP3.

# Áudio utilizado: Unknown Brain - Superhero (feat. Chris Linton) [NCS Release]

usar_pygame = True

if(usar_pygame):
    from pygame import mixer
    mixer.init()
    mixer.music.load('ex021.mp3')
    mixer.music.play()
    input('Agora você escuta? ')
else:
    import os
    os.startfile(r"ex021.mp3")
