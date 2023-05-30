# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

numero = int(input('Insira um valor inteiro entre 1-10\n : '))
contador = 0

for i in range(1,10+1):
    contador += 1
    resultado = numero * contador
    print(f'{numero} X {contador} = {resultado}')

