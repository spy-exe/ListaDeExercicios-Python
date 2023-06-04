# # Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
altura = float(input("Digite sua altura: "))

peso_homem = (72.7 * altura) - 58
peso_mulher = (62.1 * altura) - 44.7

print(f'Homem: {peso_homem:.2f}kg\n'
      f'Mulher: {peso_mulher:.2f}kg')

