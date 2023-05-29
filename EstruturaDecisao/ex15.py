# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
#   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: três lados diferentes;

l1 = float(input("Insira o valor de um lado do triangulo: "))
l2 = float(input("Insira outro valor do lado de um triangulo: "))
l3 = float(input("Insira mais um valor do lado de um triangulo: "))

triangulo = 'Os valores não formam um triângulo'

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        triangulo = 'Equilatero'
    elif l1 == l2 or l1 == l3 or l2 == l3:
        triangulo = 'Isosceles'
    else:
        triangulo = 'Escaleno'

print(triangulo)
