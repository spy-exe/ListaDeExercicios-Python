# Foram anotadas as idades e alturas de 30 alunos. 
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

alunos = 30
lista_idades = []
lista_alturas = []

for i in range(1,alunos+1):
    idade = int(input(f'[{i}/{alunos}] Insira a idade: '))
    altura = float(input(f'[{i}/{alunos}] Insira a altura: '))
    lista_idades.append(idade)
    lista_alturas.append(altura)

media_altura = sum(lista_alturas) / alunos
contador = 0

for idade, altura in zip(lista_idades, lista_alturas):
    if idade > 13 and altura < media_altura:
        contador += 1

print(f'{contador} alunos com mais de 13 anos possuem a altura inferior a media de altura.')
        