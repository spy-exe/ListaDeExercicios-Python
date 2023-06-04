# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = []

for i in range(1,4+1):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
for i in range(len(notas)):
    print(f'A {i+1}ª nota foi {notas[i]}')
print(f'A média das notas é {media:.2f}')