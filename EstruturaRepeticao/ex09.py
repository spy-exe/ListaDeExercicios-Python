# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
numero = 0

for numero in range(1,50+1):
    if numero % 2 == 1:
        print(numero, end=" ")
    else:
        continue