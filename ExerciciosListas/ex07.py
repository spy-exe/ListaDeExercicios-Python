# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
vetor = []

for x in range(1,5+1):
    numero = int(input(f'[{x}/5] Insira um número: '))
    vetor.append(numero)

multiplicacao = 1

for numero in vetor:
    multiplicacao *= numero

soma = sum(vetor)

print(vetor)
print(soma)
print(multiplicacao)