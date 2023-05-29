# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    user = input('Insira seu nome de usuário: ')
    password = input('Insira sua senha: ')
    if password == user:
        print('Sua senha não pode ser igual seu nome de usuário!')
    else:
        print('Login realizado com sucesso!')
        break