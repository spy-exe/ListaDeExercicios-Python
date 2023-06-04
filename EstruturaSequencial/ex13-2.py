# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo (M/F): ").upper()
if sexo == "M":
    formula = (72.7 * altura) - 58
    print(f'Com base na sua altura: {altura:.2f} Seu peso ideal é {formula:.2f}kg')
elif sexo == "F":
    formula = (62.1 * altura) - 44.7
    print(f'Com base na sua altura: {altura:.2f} Seu peso ideal é {formula:.2f}kg')
else:
    print("Sexo inválido!")
