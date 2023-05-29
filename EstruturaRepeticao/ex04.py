# Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacao_A = 80000
cresc_pop_A = 0.03

populacao_B = 200000
cresc_pop_B = 0.015

anos = 0

# Enquanto a populacao A for menor que a B
while populacao_A < populacao_B:
#   80.000         Taxa de crescimento 3% ao ano
    populacao_A += populacao_A * cresc_pop_A
#   200.000        Taxa de crescimento 1.5% ao ano
    populacao_B += populacao_B * cresc_pop_B

#   Incrementa o contador de anos
    anos += 1

print(f'Sera necessario {anos} anos, para a populacao A alcancar a populacao B')