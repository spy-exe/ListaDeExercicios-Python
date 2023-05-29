# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#   Par ou ímpar;
#   Positivo ou negativo;
#   Inteiro ou decimal.

n1 = float(input('- Insira um número\n : '))
n2 = float(input('- Insira outro número\n : '))
opcao = int(input('O que deseja fazer com estes números?\n\n1 - Somar\n2 - Multiplicar\n3 - Dividir\n4 - Subtrair\n5 - Potencializar\n : '))

while opcao > 5 or opcao < 1:
    print(f'Opção {opcao} inválida')
    opcao = int(input('O que deseja fazer com estes números?\n\n1 - Somar\n2 - Multiplicar\n3 - Dividir\n4 - Subtrair\n5 - Potencializar\n : '))

opcoes = ['[+] Somar','[*] Multiplicar','[/] Dividir','[-] Subtrair','[**] Potencializar']

if opcao == 1:
    resultado = n1+n2
elif opcao == 2:
    resultado = n1*n2
elif opcao == 3:
    resultado = n1/n2
elif opcao == 4:
    resultado = n1-n2
elif opcao == 5:
    resultado = n1**n2

if resultado % 2 == 0:
    mensagem1 = 'Par'
else:
    mensagem1 = 'Impar'

if resultado < 0:
    mensagem2 = 'Negativo'
else:
    mensagem2 = 'Positivo'

if resultado.is_integer():
    mensagem3 = 'Inteiro'
    resultado = round(resultado)
else:
    mensagem3 = 'Decimal'

print(f'Opção: {opcoes[opcao-1]} | Resultado: {resultado}\n'
      f'( {mensagem1} )\n'
      f'( {mensagem2} )\n'
      f'( {mensagem3} )\n')