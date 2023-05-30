# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.
vetores = []
vetor_par = []
vetor_impar = []

for _ in range(1,20+1):
    numero = int(input(''))
    if numero % 2 == 0:
        vetor_par.append(numero) # Armazena somente os numeros pares
    else:
        vetor_impar.append(numero) # Armazena somente os numeros impares
    vetores.append(numero) # Armazena todos os numeros

print('Lista dos vetores pares:')
for vetor in vetor_par:
    print(vetor)
print('Lista dos vetores impares:')
for vetor in vetor_impar:
    print(vetor)
print('Lista de todos os vetores:')
for vetor in vetores:
    print(vetor)