# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    # "Telefonou para a vítima?"
    # "Esteve no local do crime?"
    # "Mora perto da vítima?"
    # "Devia para a vítima?"
    # "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita"
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
contador = 0

classificacao = [ 'Suspeita',
                  'Cúmplice',
                  'Assassino',
                  'Inocente']

perguntas = ["Telefonou para a vítima?",
             "Esteve no local do crime?",
             "Mora perto da vítima?",
             "Devia para a vítima?",
             "Já trabalhou com a vítima?" ]

respostas = []

for i in range(1,len(perguntas)+1):
    resposta = input(f'{perguntas[i-1]} [s/n]: ').lower()
    respostas.append(resposta)

for resposta in respostas:
    if resposta == 's':
        contador += 1
    else:
        pass

if contador <= 2:
    print(classificacao[0])
elif contador < 4:
    print(classificacao[1])
elif contador == 5:
    print(classificacao[2])
else:
    print(classificacao[3])

