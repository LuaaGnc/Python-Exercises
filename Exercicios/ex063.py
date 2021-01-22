print('-' * 35)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 35)
numero_termos = int(input('Quantos termos quer mostrar? '))
print('~' * 35)

n = 0
termo_final = 0
termo_uso = 1

while numero_termos != 0:
    formula = (1 / (5) ** (1 / 2) * ((((1 + (5) ** (1 / 2)) / 2) ** n) - (((1 - (5) ** (1 / 2)) / 2) ** n)))
    print(f'{formula:.0f} -> ', end='')
    numero_termos -= 1
    n += 1
       
print('FIM')
print('~' * 35)
