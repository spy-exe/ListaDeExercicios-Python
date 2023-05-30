# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros = []
contagem = 0
pares = 0
impares = 0

for i in range(10):
    
    contagem += 1
    numero = int(input(f' [{contagem}/10] Insira um numero inteiro: '))
    numeros.append(numero)
    if numero % 2 == 1:
        impares += 1
    else:
        pares += 1
    
print(f'Quantidade de números pares: {pares}\nQuantidade de números impares: {impares}')