idade_em_dias = int(input('Insira sua idade em dias: '))

# Calcular os anos, meses e dias
anos = idade_em_dias // 365
meses = (idade_em_dias % 365) // 30
dias = (idade_em_dias % 365) % 30

# Imprimir a saída formatada
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")

print(f'anos = {idade_em_dias} // 365 = {anos}\n \n'
      f'meses = ({idade_em_dias} % 365) = {idade_em_dias % 365}\n{idade_em_dias % 365} // 30 = {meses}\n \n'
      f'dias = ({idade_em_dias} % 365) = {idade_em_dias % 365}\n{idade_em_dias % 365} % 30 = {dias}')