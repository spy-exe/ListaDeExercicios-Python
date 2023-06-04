# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   Comprar apenas latas de 18 litros;
#   Comprar apenas galões de 3,6 litros;
#   Misturar latas e galões, de forma que o desperdício de tinta seja menor.
#   Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros = area / 6
folga = litros * 1.1
latas = litros / 18
preco_latas = latas * 80
galoes = litros / 3.6
preco_galoes = galoes * 25



print(f'Você precisará de {latas:.0f} latas de tinta, que custarão R${preco_latas:.2f}')
print(f'Você precisará de {galoes:.0f} galões de tinta, que custarão R${preco_galoes:.2f}')

# Formula para misturar latas e galões de forma que o desperdício de tinta seja menor:
formula = (litros // 18) * 80 + (litros % 18 // 3.6 + 1) * 25
print(f'Você precisará de {(litros // 18) + 1:.0f} latas e {(litros % 18 // 3.6 + 1):.0f} galões de tinta, que custarão R${formula:.2f}')