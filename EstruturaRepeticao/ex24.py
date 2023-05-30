# Faça um programa que calcule o mostre a média aritmética de N notas
import math
notas = []

numero_notas = int(input('Insira o numero de notas que deseja calcular: '))

for i in range(1, numero_notas+1):
    nota = float(input(f'[{i}/{numero_notas}] Insira o valor da nota: '))
    notas.append(nota)
    
media = math.fsum(notas) / numero_notas
print(f'Media das notas: {media:.2f}')
