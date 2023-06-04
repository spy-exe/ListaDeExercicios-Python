# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite o valor do lado do quadrado: "))
area = lado ** 2 # Formula da área do quadrado: A = l²
print(f'A área do quadrado de lado {lado} é {area:.2f}')