# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input('- Insira um numero: '))
n2 = int(input('- Insira um numero: '))
n3 = int(input('- Insira um numero: '))

if n1 >= n2 and n1 >= n3:
    maior = n1
    if n2 >= n3:
        menor = n3
        medio = n2
    else:
        menor = n2
        medio = n3

elif n2 >= n1 and n2 >= n3:
    maior = n2
    if n3 > n1:
        menor = n1
        medio = n3
    else:
        menor = n3
        medio = n1

else:
    maior = n3
    if n1 >= n2:
        medio = n1
        menor = n2
    else:
        medio = n2
        maior = n1

print(f'Numeros em ordem decrescente: {maior}, {medio}, {menor}')

