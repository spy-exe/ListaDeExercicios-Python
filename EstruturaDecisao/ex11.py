# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#  Salários até R$ 280,00 (incluindo) : aumento de 20%
#  Salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#  Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#  Salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#  O salário antes do reajuste;
#  O percentual de aumento aplicado;
#  O valor do aumento;
#  O novo salário, após o aumento.

salario = float(input('- Insira seu salário atual \n: R$'))

if salario <= 280 or salario <= 700:
    if salario <= 280:
        perc = 0.2 # Reajuste de 20%
        reajuste = salario * perc
    elif salario <= 700:
        perc = 0.15 # Reajuste de 15%
        reajuste = salario * perc

if salario > 700 or salario >= 1500 or salario > 1500:
    if salario >= 1500 or salario > 700:
        perc = 0.1 # Reajuste de 10%
        reajuste = salario * perc
    if salario > 1500:
        perc = 0.05 # Reajuste de 5%
        reajuste = salario * perc

if perc == 0.2:
    perc = '20%'
elif perc == 0.15:
    perc = '15%'
elif perc == 0.10:
    perc = '10%'
else:
    perc = '5%'

print(f' Salário antes do reajuste:      R${salario:.2f}\n'
      f' Percentual de aumento aplicado: {perc}\n'
      f' Valor do aumento:               R${reajuste:.2f}\n'
      f' Novo salário após reajuste:     R${salario+reajuste:.2f}\n')

