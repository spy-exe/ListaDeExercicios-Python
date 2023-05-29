# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Insira uma letra: '))

vogal = ['a','e','i','o','u']

if letra in vogal:
    print(f'A letra: ({letra}) é uma vogal.')
else:
    print(f'A letra: ({letra}) é uma consoante.')