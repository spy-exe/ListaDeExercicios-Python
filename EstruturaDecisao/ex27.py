'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

ValorMorango = 2.5
ValorMaca = 1.8

Morango = float(input('Insira a quantidade de kg de morangos\n : ')) 
Maca = float(input('Insira a quantidade de kg de macas\n : '))

if Morango > 5:
    ValorMorango = 2.20
else:
    ValorMorango = 2.5

if Maca > 5:
    ValorMaca = 1.5
else:
    ValorMaca = 1.8

if Morango + Maca >= 8:
    ValorTotal = ((ValorMorango*Morango) + (ValorMaca*Maca))
    ValorTotal = ValorTotal - (ValorTotal * 0.10)
else:
    ValorTotal = ValorMorango * Morango + ValorMaca * Maca


print(f'Quantidade de morangos(kg): {Morango}\n'
      f'Quantidade de macas(kg): {Maca}\n'
      f'Valor total: R${ValorTotal}')