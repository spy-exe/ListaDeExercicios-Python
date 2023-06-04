# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   O produto do dobro do primeiro com metade do segundo .
#   A soma do triplo do primeiro com o terceiro.
#   O terceiro elevado ao cubo.

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

calculo1 = (n1 * 2) * (n2 / 2)
calculo2 = (n1 * 3) + (n2 / 3)
calculo3 = n2 ** 3

print(f'O produto do dobro do primeiro com metade do segundo é {calculo1}\n'
      f'A soma do triplo do primeiro com o terceiro é {calculo2}\n'
      f'O terceiro elevado ao cubo é {calculo3}')
