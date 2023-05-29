# Faça um programa que leia 5 números e informe o maior número.

numeros = []

for i in range(5):
    numero = float(input('Insira um numero: '))
    numeros.append(numero)

print(f'Dentre os numeros {numeros}, o maior numero e: {max(numeros)}')