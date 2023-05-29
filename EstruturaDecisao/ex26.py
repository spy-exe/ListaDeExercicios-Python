''' 
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool: até 20 litros desconto de 3% por litro, acima de 20 litros desconto de 5% por litro 
Gasolina: até 20 litros desconto de 4% por litro, acima de 20 litros desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''


LitrosVendidos = float(input('Quantos litros deseja abastecer?\n : '))
TipoCombustivel = input('Alcool ou Gasolina? [A/G]\n : ').upper()

if TipoCombustivel == 'A':
    ValorCombustivel = 1.9
    Combustivel = 'Alcool'

elif TipoCombustivel == 'G':
    ValorCombustivel = 2.5
    Combustivel = 'Gasolina'
else:
    print(f'Opção {TipoCombustivel} é inválida.')

Preco = ValorCombustivel * LitrosVendidos

if LitrosVendidos > 20 and TipoCombustivel == 'A':
    Desconto = 0.05
else:
    Desconto = 0.03

if LitrosVendidos > 20 and TipoCombustivel == 'G':
    Desconto = 0.06
else:
    Desconto = 0.02

print("======== Nota fiscal ========\n"
      f'Tipo de combustivel: {Combustivel}\n'
      f'Litros vendidos: {LitrosVendidos} L\n'
      f'Valor do Litro: R${ValorCombustivel:.2f}\n'
      f'Desconto Aplicado: {Desconto*100:.0f}%\n\n'
      f'Valor a pagar: R${Preco-(Preco*Desconto):.2f}\n=============================\n')


