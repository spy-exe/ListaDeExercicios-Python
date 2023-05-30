# Altere o programa anterior para mostrar no final a soma dos números.

import math

numeros = []

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

if n1 < n2:
    for num in range(n1, n2 + 1):
        numeros.append(num)
        soma = math.fsum(numeros)
else:
    for num in range(n1, n2 - 1, -1):
        numeros.append(num)
        soma = math.fsum(numeros)
        
print(soma)