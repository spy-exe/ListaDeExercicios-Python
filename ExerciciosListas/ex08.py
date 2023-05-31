# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.
pessoas = 5
vetor_idade = []
vetor_altura = []

for i in range(1,pessoas+1):
    idade = int(input(f'[{i}/{pessoas}] Insira a idade: '))
    altura = float(input(f'[{i}/{pessoas}] Insira a altura: '))
    vetor_idade.append(idade)
    vetor_altura.append(altura)

vetor_idade = ", ".join(map(str,vetor_idade[::-1]))
vetor_altura = ", ".join(map(str,vetor_altura[::-1]))

print(f'Idade: {vetor_idade}' )
print(f'Altura: {vetor_altura}' )