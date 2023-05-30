# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vogais = 'AEIOU'
vetor = []
# Ler o vetor de 10 caracteres
for _ in range(1,10+1):
    caractere = input(f'Digite o {_} caractere: ').upper()
    if len(caractere) > 1:
        print('Insira apenas um caractere!')
        continue
    vetor.append(caractere)

# Contar as consoantes e imprimir
consoantes = []
contador = 0

for caractere in vetor:
    if caractere not in vogais:
        consoantes.append(caractere)
        contador += 1

# Imprimir resultado
consoantes = ', '.join(map(str, consoantes)) # Arrumando esteticamente as consoantes
print(f"Foram lidas {contador} consoantes:"
      f"Letras: {consoantes}")
