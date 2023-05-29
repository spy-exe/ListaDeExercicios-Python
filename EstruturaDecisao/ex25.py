''' 
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
pontos = 0

print('Responda as seguintes perguntas: [s/n]')
p1 = input('Telefonou para a vítima?\n: ').lower()
p2 = input('Esteve no local do crime?\n: ').lower()
p3 = input('Mora perto da vítima?\n: ').lower()
p4 = input('Devia para a vítima?\n: ').lower()
p5 = input('Já trabalhou com a vítima?\n: ').lower()

if p1 == 's':
    pontos += 1
else:
    pass
if p2 == 's':
    pontos += 1
else:
    pass
if p3 == 's':
    pontos += 1
else:
    pass
if p4 == 's':
    pontos += 1
else:
    pass
if p5 == 's':
    pontos += 1
else:
    pass

if pontos == 2:
    classificacao = 'Suspeito'
elif pontos <= 4:
    classificacao = 'Cumplice'
elif pontos == 5:
    classificacao = 'Assasino'
else:
    classificacao = 'Inocente'

print(classificacao)