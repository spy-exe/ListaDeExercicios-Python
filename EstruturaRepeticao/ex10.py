# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

if n1 < n2:
    for num in range(n1, n2 + 1):
        print(num, end=' ')
else:
    for num in range(n1, n2 - 1, -1):
        print(num, end=' ')