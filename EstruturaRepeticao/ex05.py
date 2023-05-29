# Altere o programa anterior permitindo ao usuário informar as populações 
# e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

while True:
    Pop_Inicial_A = int(input('Insira a populacao inicial de A:\n : '))
    if Pop_Inicial_A < 0:
        print('Insira um valor valido.')
        continue
    Cresc_Pop_A = float(input('Insira a % de crescimento da populacao A:\n : '))
    if Cresc_Pop_A < 0:
        print('Insira um valor valido.')
        continue

    Pop_Inicial_B = int(input('Insira a populacao inicial de B:\n : '))
    if Pop_Inicial_B < 0:
        print('Insira um valor valido.')
        continue
    Cresc_Pop_B = float(input('Insira a % de crescimento da populacao B:\n : '))
    if Cresc_Pop_B < 0:
        print('Insira um valor valido.')
        continue

    Cresc_Pop_A = Cresc_Pop_A / 100
    Cresc_Pop_B = Cresc_Pop_B / 100

    anos = 0

    # Enquanto a populacao A for menor que a B
    while Pop_Inicial_A < Pop_Inicial_B:

        Pop_Inicial_A += Pop_Inicial_A * Cresc_Pop_A
        Pop_Inicial_B += Pop_Inicial_B * Cresc_Pop_B

    # Incrementa o contador de anos
        anos += 1

    print(f'Serao necessario {anos} anos, para a populacao A alcancar a populacao B')
    pergunta = input('Deseja realizar a operacao novamente? S/N\n : ').lower()
    if pergunta == 's':
        continue
    elif pergunta == 'n':
        print('Programa encerrado.')
        break
    else:
        print(f"Opcao {pergunta} invalida.")
