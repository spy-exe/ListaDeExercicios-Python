# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dias_semana = [
    'Domingo',
    'Segunda',
    'Terça',
    'Quarta',
    'Quinta',
    'Sexta',
    'Sábado'
]

dia = int(input('- Insira o dia da semana em numero: '))

if 1 <= dia <= 7:
    dia_semana = dias_semana

print(f'O dia que você escolheu é {dia_semana}')