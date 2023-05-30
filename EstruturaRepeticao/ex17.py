# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input('Insira um numero inteiro: '))

fatorial = 1

if numero < 0:
    print('Nao pode-se fatorar numeros negativos!')
elif numero == 0:
    print('O fatorial de um numero 0 e igual a 0')
else:
    for i in range(1, numero+1):
        fatorial *= i

    print(fatorial)
