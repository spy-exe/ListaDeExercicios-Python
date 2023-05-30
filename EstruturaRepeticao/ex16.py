# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.

while True:
    n = int(input('Insira um valor maior que 500: '))
    if n < 500:
        continue

    termo1 = 1
    termo2 = 1

    for i in range(1,n+1):
        prox_termo = termo1 + termo2
        termo1 = termo2
        termo2 = prox_termo
        print(prox_termo)
    break
    
        
