# Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. 

lista_vetor_1 = []
lista_vetor_2 = []


for loop_vetor1 in range(1,10+1):
    vetor1 = input(f'[{loop_vetor1}/10] Insira o valor do elemento do vetor 1: ')
    lista_vetor_1.append(vetor1)

for loop_vetor2 in range(1,10+1):
    vetor2 = input(f'[{loop_vetor2}/10] Insira o valor do elemento do vetor 2: ')
    lista_vetor_2.append(vetor2)

for vetor1, vetor2 in zip(lista_vetor_1, lista_vetor_2):
    print(vetor1, vetor2)