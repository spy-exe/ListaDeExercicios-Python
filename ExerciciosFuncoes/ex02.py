
lastName = input(f'Last Name: ')
def fullNames():
    namelist = []
    global count  # Declarar a variável 'count' como global
    count = 0
    while True:
        count += 1
        
        firstName = input(f'{count} First Name: ')
        namelist.append(firstName)
        if firstName == '0':
            break

    for firstName in namelist:
          # Corrigir a linha para remover o último elemento
        if firstName == '0':
            pass
        else:
            print(f'{firstName} {lastName}')
    return ""

print(fullNames())  # Chamar a função e imprimir o resultado