# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

#               0         1           2       3      4       5      6        7        8         9         10         11
lista_meses = ['Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
lista_temperaturas = []

for i in range(1,12+1):
    temperatura_mensal = float(input(f'Insira a temperatura media de {"".join(map(str, lista_meses[i-1]))}: '))
    lista_temperaturas.append(temperatura_mensal)

media_anual = sum(lista_temperaturas) / 12

lista_temperaturas_acima = []
lista_meses_acima = []

for i in range(len(lista_temperaturas)):
    if lista_temperaturas[i] > media_anual:
        lista_temperaturas_acima.append(lista_temperaturas[i])
        lista_meses_acima.append(lista_meses[i])

print('Temperaturas e meses acima da média anual:')
print('     Mês       |    Temperatura    ')

for mes, temperatura in zip(lista_meses_acima, lista_temperaturas_acima):
    print(f'{mes} - {temperatura}°C')
