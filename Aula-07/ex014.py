# Curso Python 07
# ---Desafio 14---
# Escreva um programa que converta uma temperatura digitando 
# em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Digite a temperatura em ºC: '))

print(f'{temp}ºC corresponde a {(9*temp+160)/5}ºF e a {temp+273.15}ºK')
