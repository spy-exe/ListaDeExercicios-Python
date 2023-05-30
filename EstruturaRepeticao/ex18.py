# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
import math
numeros = []

n = int(input('Escolha uma quantidade de numeros: '))

for i in range(1,n):
    numero = float(input(f'[{i}/{n}] Insira um numero: '))
    numeros.append(numero)
    
    maior_valor = max(numeros)
    menor_valor = min(numeros)
    soma = math.fsum(numeros)

print(f'Menor valor: {menor_valor}\nMaior valor: {maior_valor}\nSoma dos valores: {soma}')