# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Digite o valor da sua hora de trabalho: R$"))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_mensal = valor_hora * horas_trabalhadas

print(f'O valor do seu salário no mês é R${salario_mensal:.2f}')