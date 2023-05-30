# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas
# e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

from math import fsum # Melhor alocamento de memoria, importar somente a funcao utilizada.

lista_temperaturas = []
n_temperaturas = int(input('Informe a quantidade de temperaturas: '))
tipo_temperatura = str(input('Insira o tipo de temperatura\nC - Celsius, F - Fahrenheit, K - Kelvin\n : ')).upper()



for _ in range(1,n_temperaturas+1):
    temperatura = float(input(f'[{_}/{n_temperaturas}] Informe o valor da temperatura {_}: '))
    lista_temperaturas.append(temperatura)

media_temperaturas = fsum(lista_temperaturas) / n_temperaturas
temperatura_max = max(lista_temperaturas)
temperatura_min = min(lista_temperaturas)


print(f'Media de temperatura: {media_temperaturas:.1f}°{tipo_temperatura}\n'
      f'Temperatura maior: {temperatura_max:.1f}°{tipo_temperatura}\n'
      f'Temperatura menor: {temperatura_min:.1f}°{tipo_temperatura}\n')