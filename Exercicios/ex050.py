soma_valores = 0
contagem_valores = 1
for valores in range(1, 7):
    valores = int(input(f'Digite o {contagem_valores}º valor: '))
    if valores % 2 == 0:
        soma_valores += valores
    contagem_valores += 1
print(f'Você informou {contagem_valores} números e a soma foi {soma_valores}')
