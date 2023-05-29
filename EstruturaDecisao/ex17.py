# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
# Obs O ano deve ser divisível por 4.
# O ano não deve ser divisível por 100,
# A menos que também seja divisível por 400.


ano = int(input("Digite o ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    bissexto = 'Sim'
else:
    bissexto = 'Não'

print(f'\n - Ano: {ano} \n - Bissexto: {bissexto}\n')