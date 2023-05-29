# Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#
#  Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#  Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input("- Insira o valor do saque\n- Limite:\n Min. 10 reais\n Max. 600 reais\n \n : "))

while saque < 10 or saque > 600:
    print("O valor deve ser menor que 600 reais\nE maior que 10 reais.")
    saque = int(input(" : "))

notas_100 = saque // 100 
resto = saque % 100
notas_50 = resto // 50
resto = resto % 50
notas_10 = resto // 10
resto = resto % 10
notas_5 =  resto // 5
resto = resto % 5
notas_1 =  resto // 1

print(f'Para sacar a quantia de R${saque:.2f} sera necessario\n'
      f'{notas_100:.0f} notas de 100.\n'
      f'{notas_50:.0f} notas de 50.\n'
      f'{notas_10:.0f} notas de 10.\n'
      f'{notas_5:.0f} notas de 5.\n'
      f'{notas_1:.0f} notas de 1.\n')