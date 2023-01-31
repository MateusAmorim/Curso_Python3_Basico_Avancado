frase = 'O python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido Van Rossum.'
qtd_aparecel_mais_vezes = 0
letra_aparecel_mais_vezes = ''

i = 0
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    qtd_aparecel_mais_vezes_atual = frase.count(letra_atual)

    if qtd_aparecel_mais_vezes < qtd_aparecel_mais_vezes_atual:
        qtd_aparecel_mais_vezes = qtd_aparecel_mais_vezes_atual
        letra_aparecel_mais_vezes = letra_atual
    i += 1

print(
    'A letra que aparecel mais vezes foi '
    f'"{letra_aparecel_mais_vezes}" que apareceu '
    f'{qtd_aparecel_mais_vezes} vezes.'
)
