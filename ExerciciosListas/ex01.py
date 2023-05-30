# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = []

for _ in range(1,5+1):
    numero = int(input(f'[{_}/5] Informe um numero: '))
    vetor.append(numero)

print('Numeros informados: ')
for numero in vetor:
    print(numero)