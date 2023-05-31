# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

lista_vetor_1 = []
lista_vetor_2 = []
lista_vetor_3 = []


for loop_vetor1 in range(1,10+1):
    vetor1 = input(f'[{loop_vetor1}/10] Insira o valor do elemento do vetor 1: ')
    lista_vetor_1.append(vetor1)

for loop_vetor2 in range(1,10+1):
    vetor2 = input(f'[{loop_vetor2}/10] Insira o valor do elemento do vetor 2: ')
    lista_vetor_2.append(vetor2)

for loop_vetor3 in range(1,10+1):
    vetor3 = input(f'[{loop_vetor3}/10] Insira o valor do elemento do vetor 3: ')
    lista_vetor_3.append(vetor3)

for vetor1, vetor2, vetor3 in zip(lista_vetor_1, lista_vetor_2, lista_vetor_3):
    print(vetor1, vetor2, vetor3)