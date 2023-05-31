# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
numeros = 10
lista_vetor_a = []

for i in range(1,numeros+1):
    numero = int(input(f'[{i}/{numeros}] Insira um numero inteiro: '))
    numero **= 2
    lista_vetor_a.append(numero)

soma = sum(lista_vetor_a)
print(soma)

