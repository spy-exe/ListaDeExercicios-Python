# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []

for _ in range(1,10+1):
    numero = int(input(f'[{_}/10] Informe 10 numeros: '))
    vetor.append(numero)
 
vetor = vetor[::-1] # Deixa os itens da lista de forma reversa

print('Numeros informados: ')
for numero in vetor:
    print(numero)
