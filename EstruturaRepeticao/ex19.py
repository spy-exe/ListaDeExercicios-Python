# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

import math
numeros = []

n = int(input('Escolha uma quantidade de numeros: '))


for i in range(1,n):
    while True:
        numero = float(input(f'[{i}/{n}] Insira um numero: '))
        if numero < 0 or numero > 1000:
            print('Escolha um valor entre 0-1000!')
            continue
        
        numeros.append(numero)
        maior_valor = max(numeros)
        menor_valor = min(numeros)
        soma = math.fsum(numeros)
        break

print(f'Menor valor: {menor_valor}\nMaior valor: {maior_valor}\nSoma dos valores: {soma}')