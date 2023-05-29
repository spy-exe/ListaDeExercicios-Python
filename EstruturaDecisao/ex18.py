# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Insira uma data no formato: dd/mm/aaaa:\n - ")

def dividir_data(data):
    separador = data.split("/")
    dia = data[0]
    mes = data[1]
    ano = data[2]

if "/" in data:
    print(f"Você inseriu uma data no formato válido: {data}") 
else:
    print(f"Você inseriu uma data em um formato inválido: {data}")