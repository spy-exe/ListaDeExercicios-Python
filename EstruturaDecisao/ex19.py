# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#   326 = 3 centenas, 2 dezenas e 6 unidades
#   12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16



n = int(input("Insira um valor inteiro menor ou igual a 1000:\n : "))

nome_centena = 'centena'
nome_dezena = 'dezena'
nome_unidade = 'unidade'

centena = n // 100
dezena = (n % 100) // 10
unidade = (n % 100) % 10

while n > 1000:
    print("\nIncorreto: Insira um valor inteiro menor ou igual a 1000!")
    n = int(input(" : "))

if centena > 1:
        nome_centena = 'centenas'
if dezena > 1:
        nome_dezena = 'dezenas'
if unidade > 1:
        nome_unidade = 'unidades'

print(f"Número: [ {n} ]"
    f"\n{centena} {nome_centena}"
    f"\n{dezena} {nome_dezena}"
    f"\n{unidade} {nome_unidade}")
        
