# # Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

lista_numeros=[]

fatorial = 1

numero = int(input('Insira um numero para fazer o fatorial: '))

for i in range(1, numero+1):
    fatorial *= i
    lista_numeros.append(i)

lista_numeros = lista_numeros[::-1] # Deixando a lista em ordem decrescecnte
lista_numeros = " . ".join(map(str,lista_numeros)) # Formatando a lista da forma exigida com "." de espacamento.

print(f'{numero}! = {lista_numeros} = {fatorial}')