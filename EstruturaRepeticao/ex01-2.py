# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    nota = float(input('Insira uma nota entre 0 - 10\n : '))
    if nota < 0 or nota > 10:
        print('Insira uma nota valida!')
    else:
        print(f'Nota valida! {nota}')
        break