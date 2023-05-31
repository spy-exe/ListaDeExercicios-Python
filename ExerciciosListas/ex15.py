# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando
# for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
#
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
#
# Encerre o programa com uma mensagem;



lista_notas = []

contador = 0
while True:
    contador += 1
    nota = float(input(f'{contador} - Insira uma nota: '))
    lista_notas.append(nota)
    if nota == -1:
        break

soma = sum(lista_notas)
media = soma / contador

notas_acima = 0
notas_abaixo = 0
for nota in lista_notas:
    if nota > media:
        notas_acima += 1
    elif nota < 7:
        notas_abaixo += 1

print(f'Soma das notas: {soma}\n'
      f'Média das notas calculadas: {media}\n'
      f'Notas acima da média calculada: {notas_acima}\n'
      f'Notas abaixo de 7: {notas_abaixo}\n')