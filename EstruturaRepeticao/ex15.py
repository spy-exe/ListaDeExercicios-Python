# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input("Insira o valor de n: "))

termo1 = 1
termo2 = 1

for i in range(2, n):
    proximo_termo = termo1 + termo2
    print(proximo_termo)

    termo1 = termo2
    termo2 = proximo_termo
