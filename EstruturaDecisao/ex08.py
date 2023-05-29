# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto_1 = float(input('- Insira o valor do primeiro produto: R$'))
produto_2 = float(input('- Insira o valor do segundo produto: R$'))
produto_3 = float(input('- Insira o valor do terceiro produto: R$'))

menor_preco = min(produto_1,produto_2,produto_3)

if menor_preco == produto_1:
    print(f'Voce deve comprar o primeiro produto')
elif menor_preco == produto_2:
    print(f'Voce deve comprar o segundo produto')
else:
    print(f'Voce deve comprar o terceiro produto')