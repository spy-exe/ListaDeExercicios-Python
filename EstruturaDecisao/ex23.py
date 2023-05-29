# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
numero = float(input('Insira um numero inteiro ou decimal\n : '))

if numero.is_integer() == False:
    mensagem = 'Decimal'
else:
    mensagem = 'Inteiro'
    numero = round(numero)


print(f'O numero {numero} e {mensagem}')