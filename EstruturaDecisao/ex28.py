# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
# cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

fileduplo = 4.9
alcatra =  5.9
picanha = 6.9

meats = ['File Duplo', 'Alcatra', 'Picanha']

quantity = float(input('Insert the quantity in kg, for the meat \n : '))
meat = int(input('Choice the type of meat:\n 1 = File Duplo, 2 = Alcatra, 3 = Picanha\n : '))
payment = input('What is the payment type?\nType: Card or Money\n : ').lower()

if quantity > 5:
    fileduplo = 5.8
    alcatra = 6.8
    picanha = 7.8
else:
    pass

if meat == 1:
    price = quantity * fileduplo
elif meat == 2:
    price = quantity * alcatra 
elif meat == 3:
    price = quantity * picanha
else:
    print(f'Invalid option: {meat}')

if payment == 'card':
    discount = price * 0.05

print(f'------- Fiscal note -------\nMeat type: {meats[meat-1]} | Quantity: {quantity} kg'
      f'\nTotal price: ${price:.2f}'
      f'\nPayment Type: {payment.upper()}'
      f'\nDiscount value: ${discount:.2f}'
      f'\nFinal price: ${price-discount:.2f}\n')
