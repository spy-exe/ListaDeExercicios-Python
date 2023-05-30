# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes
# e limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    numero = int(input('Insira um numero com as condicoes: \n- Inteiro e positivo e menor que 16\n : '))
    if numero < 0 or numero > 16:
        print('Insira um numero positivo!')
        continue
    elif numero >= 16:
        print('Insira um numero menor que 16!')
        continue

    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(fatorial)



# numero = int(input('Insira um numero inteiro: '))

# fatorial = 1

# if numero < 0:
#     print('Nao pode-se fatorar numeros negativos!')
# elif numero == 0:
#     print('O fatorial de um numero 0 e igual a 0')
# else:
#     for i in range(1, numero+1):
#         fatorial *= i

#     print(fatorial)