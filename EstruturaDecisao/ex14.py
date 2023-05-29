# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
# A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0            A
#  Entre 7.5 e 9.0             B
#  Entre 6.0 e 7.5             C
#  Entre 4.0 e 6.0             D
#  Entre 4.0 e zero            E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))

media = (n1+n2) / 2


if media <= 4:
    conceito = 'E'
    mensagem = 'Reprovado'
elif media <= 6:
    conceito = 'D'
    mensagem = 'Reprovado'
elif media <= 7.5:
    conceito = 'C'
    mensagem = 'Aprovado'
elif media <= 9.0:
    conceito = 'B'
    mensagem = 'Aprovado'
else:
    conceito = 'A'
    mensagem = 'Aprovado'

print(f'Média de aproveitamento: {media:.2f}\nConceito: {conceito}\n{mensagem}')