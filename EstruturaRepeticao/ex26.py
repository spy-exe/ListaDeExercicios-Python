# Numa eleição existem três candidatos.
# Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato1 = 0
candidato2 = 0
candidato3 = 0

eleitores = int(input('Insira o numero total de eleitores: '))

for i in range(1, eleitores+1):
    voto = int(input(f'[{i}/{eleitores}] Vote nos cadidatos:\n'
                       'Cadidato 1: 141\n'
                       'Cadidato 2: 142\n'
                       'Cadidato 3: 143\n Insira seu voto: '))
    if voto == 141:
        candidato1 += 1
    elif voto == 142:
        candidato2 += 1
    elif voto == 143:
        candidato3 += 1
    else:
        print(f'Numero {voto} Invalido.')


print(f'Candidato 1: {candidato1} voto(s)\n'
      f'Candidato 2: {candidato2} voto(s)\n'
      f'Candidato 3: {candidato3} voto(s)\n')