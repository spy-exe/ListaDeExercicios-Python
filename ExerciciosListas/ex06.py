# Faça um Programa que peça as quatro notas de 10 alunos
# calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.
medias = []
n_alunos = 10
n_notas = 4

for x in range(1,n_alunos+1):
    notas = []
    
    for y in range(1,n_notas+1):
        nota = float(input(f'Insira a nota {y} do Aluno {x}\n : '))
        notas.append(nota)
    
    media = sum(notas) / n_notas
    medias.append(media)

alunos_aprovados = 0
for media in medias:
    if media >= 7:
        alunos_aprovados += 1

print(f'Numero de alunos aprovados: {alunos_aprovados}')
        



