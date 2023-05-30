# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

n = int(input('Insira um número: '))

# Verifica se o número é menor que 2, que não é considerado primo
if n < 2:
    print(f'{n} não é um número primo.')
else:
    # Verifica se o número é divisível por algum número entre 2 e a sua metade
    for i in range(2, n//2 + 1):
        if n % i == 0:
            print(f'{n} não é um número primo.')
            break
        else:
            print(f'{n} é um número primo.')
