# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
from math import fsum
lista_notas = []
contador = 0

for _ in range(1,4+1):
    nota = float(input(f'[{_}/4] Informe uma nota: '))
    lista_notas.append(nota)

print('Lista de Notas:')
for nota in lista_notas:
    contador += 1
    print(f'Nota {contador}: {nota}')
    media = fsum(lista_notas)/4
print(f'Media: {media}')


