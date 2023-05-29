""" 
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00  
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
"""
inss = 0.1
fgts = 0.11

valor_hora = float(input('Insira o seu salario por hora: '))
qnt_horas = int(input('Insira quantas horas voce trabalha por mes: '))

sal_bruto = valor_hora * qnt_horas

if sal_bruto <= 900:
    ir = 0
elif sal_bruto <= 1500:
    ir = 0.05
elif sal_bruto <= 2500:
    ir = 0.1
elif sal_bruto > 2500:
    ir = 0.2

sal_liquido = sal_bruto - (sal_bruto*(inss+fgts+ir))

print(f'\n\n    Salario bruto: (R${valor_hora} * {qnt_horas}h)                : R${sal_bruto:.2f}\n'
      f'    Imposto de renda: ({ir*100:.0f}%)                       : R${sal_bruto*ir:.2f}\n'
      f'    INSS (10%)                                    : R${sal_bruto*inss:.2f}\n'
      f'    FGTS (11%)                                    : R${sal_bruto*fgts:.2f}\n'
      f'    Total de descontos ({(inss+fgts+ir)*100:.0f}%)                      : R${sal_bruto*(inss+fgts+ir):.2f}\n'
      f'    Salario Liquido                               : R${sal_liquido:.2f}\n')