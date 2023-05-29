# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

numero = int(input('Insira um numero: \n : '))

if numero % 2 == 0:
    numero = 'Par'
else:
    numero = 'Impar'

print(numero)