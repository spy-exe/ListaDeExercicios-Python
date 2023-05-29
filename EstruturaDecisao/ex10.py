# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = str(input('- Em qual turno você estuda? \n M = Matutino, V = Vespertino, N = Noturno\n\n : '))
nome = str(input('- Insira seu nome\n\n : '))


if turno == 'M' or turno == 'V' or turno == 'N':
    if turno == 'M':
        msg = 'Bom dia!'
    elif turno == 'V':
        msg = 'Boa tarde!'
    elif turno == 'N':
        msg = 'Boa noite!'
    print(f'{msg} {nome}.')
else:
    print(f'Turno {turno} inválido!')
