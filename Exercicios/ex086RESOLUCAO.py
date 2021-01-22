matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for numero in range(0, 3):
    for contador in range(0, 3):
        matriz[numero][contador] = int(input(f'Digite um valor para [{numero}, {contador}]'))

print('-=' * 30)

for numero in range(0, 3):
    for contador in range(0, 3):
        print(f'[{matriz[numero][contador]}]:^5', end = '')
    print()
