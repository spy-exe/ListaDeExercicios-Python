# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

sex_list = [
    '1 - Masculino',
    '2 - Feminino',
    '3 - Transgenero',
    '4 - Prefiro nao dizer',
]

status_list = [
    '1 - Solteiro(a)',
    '2 - Casado(a)',
    '3 - Viuvo(a)',
    '4 - Divorciado(a)',
]

while True:
    name = input("Insira seu nome: \n : ")
    if len(name) < 3:
        print('Seu nome deve haver no minimo 3 caracteres.')
        continue

    age = int(input('Insira sua idade: \n : '))
    if age < 0 or age > 150:
        print('Insira uma idade valida. 0-150 anos.')
        continue

    salary = float(input('Insira seu salario: \n $'))
    if salary < 0:
        print('Insira um salario maior que zero!')
        continue

    sex = int(input(f'Insira seu sexo: \n{sex_list}\n : '))
    if sex < 1 and sex > 4:
        print(f'Entrada {sex} invalida, escolha uma opcao valida.')
        continue
    
    status = int(input(f'Insira seu estado civil: \n{status_list}\n : '))
    if status < 1 and status > 4:
        print(f'Entrada {status} invalida, escolha uma opcao valida.')
        continue

    print(f'Nome: {name} \nIdade: {age}' 
          f'\nSalario: ${salary:.2f}'
          f'\nSexo: {sex_list[sex-1]}'
          f'\nEstado Civil: {status_list[status-1]}')
    break