# Faça um programa que peça para n pessoas a sua idade
# Ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
import math
litas_idades = [] # Cria uma lista com a idade das pessoas.

n_pessoas = int(input('Insira a quantidade de pessoas: '))

for i in range(1,n_pessoas+1):
    while True:
        idade = int(input(f'[{i}/{n_pessoas}] Insira a idade da pessoa {i}: ')) 
        if idade < 0:
            print('A idade nao pode ser menor que 0!')
            continue
        else:
            break
    litas_idades.append(idade) # Guarda a informacao da idade da pessoa inserida.

media_idade = math.fsum(litas_idades) / n_pessoas

if media_idade <= 25:
    turma = 'Jovem'
elif media_idade > 60:
    turma = 'Idosa'
else:
    turma = 'Adulta'

print(f'A média de idade da turma varia entre: {media_idade} anos'
      f'\nPortanto é considerada {turma}')