# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Digite sua altura: "))

formula = (72.7 * altura) - 58

print(f'Com base na sua altura: {altura:.2f} Seu peso ideal é {formula:.2f}kg')