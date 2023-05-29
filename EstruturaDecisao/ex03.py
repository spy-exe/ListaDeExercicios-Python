# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

genero = str(input('Insira seu gênero:\nF - Feminino \nM - Masculino\n'))

if genero == 'M':
    print(f'Gênero masculino')
elif genero == 'F':
    print(f'Gênero feminino')
else:
    print(f'Gênero inserido {genero} inválido')
