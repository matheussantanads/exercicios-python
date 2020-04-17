# Curso Python 12
# ---Desafio 43---
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status

peso = float(input('Dgite seu peso: '))
altu = float(input('Digite sua altura: '))
imc = peso/(altu**2)

print(f'Seu IMC é {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
