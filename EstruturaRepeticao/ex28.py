# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.
import math

lista_custo_cds = []

numero_cds = int(input('Insira a quantidade de CDs: '))

for i in range(1,numero_cds+1):
    custo_cd = float(input(f'[{i}/{numero_cds}] Insira o valor gasto no CD {i}: $'))
    lista_custo_cds.append(custo_cd)

media_custo = math.fsum(lista_custo_cds) / numero_cds
print(f'A media de custo de cada CD foi de ${media_custo:.2f}')