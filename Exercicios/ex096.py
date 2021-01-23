def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg:.2f}x{comp:.2f} é de {area} m^2')

print('Controle de Terrenos')
print('-' * 20)

larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
