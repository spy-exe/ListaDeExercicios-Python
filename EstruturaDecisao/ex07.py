# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('- Insira um numero: '))
n2 = int(input('- Insira um numero: '))
n3 = int(input('- Insira um numero: '))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2

if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

print(f'O número maior é: {maior}\n'
      f'O número menor é: {menor}')


"""
# Codigo limpo.

n1 = int(input('- Insira um numero: '))
n2 = int(input('- Insira um numero: '))
n3 = int(input('- Insira um numero: '))

maior = max(n1,n2,n3)
menor = min(n1,n2,n3)

print(f'O número maior é: {maior}\n'
      f'O número menor é: {menor}')
""" 
