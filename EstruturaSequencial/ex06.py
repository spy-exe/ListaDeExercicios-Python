# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio ** 2 # Formula da área do círculo: A = π * r²
print(f'A área do círculo de raio {raio} é {area:.2f}')