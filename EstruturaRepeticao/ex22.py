# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
n = int(input('Insira um número: '))

# Verifica se o número é menor que 2, que não é considerado primo
if n < 2:
    print(f'{n} não é um número primo.')
else:
    divisores = []
    # Verifica se o número é divisível por algum número entre 2 e a sua metade
    for i in range(2, n//2 + 1):
        if n % i == 0:
            divisores.append(i)

    if len(divisores) > 0:
        print(f'{n} não é um número primo. E é divisível por: {divisores}.')
    else:
        print(f'{n} é um número primo.')