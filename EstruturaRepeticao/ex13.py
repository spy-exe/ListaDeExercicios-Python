# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

base = float(input('Insira o valor da base: '))
expoente = int(input('Insira o valor do expoente: '))

resultado = 1

for i in range(expoente):
    # resultado = base * resultado
    resultado *= base


print(resultado)