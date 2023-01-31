nome = 'Mateus'
altura = 1.75
peso = 70
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Mateus tem 1.75 de altura,
# pesa 70 Kg e seu IMC é
# 22.86
