# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# Formula da conversão: F = C * 1.8 + 32

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 1.8 + 32
print(f'A temperatura em Fahrenheit é {fahrenheit:.2f}')