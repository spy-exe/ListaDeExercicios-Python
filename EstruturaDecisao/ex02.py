# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

value = int(input("- Insira um numero: "))

if value < 0:
    print(f'O valor {value} é negativo. [-]')
elif value > 0:
    print(f'O valor {value} é positivo. [+]')