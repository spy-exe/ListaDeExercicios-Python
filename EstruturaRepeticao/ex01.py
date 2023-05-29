# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Insira uma nota entre 0 - 10\n : '))

while nota < 0 or nota > 10:
    print('Informe um valor valido!')
    nota = float(input('Insira uma nota entre 0 - 10\n : '))