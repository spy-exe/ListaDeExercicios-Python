# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   Comprar apenas latas de 18 litros;
#   Comprar apenas galões de 3,6 litros;
#   Misturar latas e galões, de forma que o desperdício de tinta seja menor.
#   Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

# Tamanho da área a ser pintada
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Cálculo da quantidade de tinta necessária com 10% de folga
litros_necessarios = math.ceil(area / 6 * 1.1)

# Cálculo da quantidade de latas de 18 litros e respectivo preço
latas = math.ceil(litros_necessarios / 18)
preco_latas = latas * 80.00

# Cálculo da quantidade de galões de 3,6 litros e respectivo preço
galoes = math.ceil(litros_necessarios / 3.6)
preco_galoes = galoes * 25.00

# Cálculo da quantidade mista de latas e galões
latas_mistas = int(litros_necessarios / 18)
resto = litros_necessarios % 18
galoes_mistos = math.ceil(resto / 3.6)
preco_misto = (latas_mistas * 80.00) + (galoes_mistos * 25.00)

# Exibição dos resultados
print("Situação 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas: ", latas)
print("Preço total: R$ ", preco_latas)

print("\nSituação 2: Comprar apenas galões de 3,6 litros")
print("Quantidade de galões: ", galoes)
print("Preço total: R$ ", preco_galoes)

print("\nSituação 3: Misturar latas e galões")
print("Quantidade de latas: ", latas_mistas)
print("Quantidade de galões: ", galoes_mistos)
print("Preço total: R$ ", preco_misto)
