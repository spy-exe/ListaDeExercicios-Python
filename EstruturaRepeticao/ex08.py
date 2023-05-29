# Faça um programa que leia 5 números e informe a soma e a média dos números.
import math

numeros = []

for i in range(5):
    numero = float(input('Insira um numero: '))
    numeros.append(numero)
    soma = math.fsum(numeros)
    media = soma / 5

print(soma,media)