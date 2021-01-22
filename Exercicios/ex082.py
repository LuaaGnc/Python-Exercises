lista_completa = []
lista_pares = []
lista_impares = []

while True:
    numero = int(input('Digite um número: '))
    escolha = str(input('Quer continuar? [S/N] ').upper().strip())

    lista_completa.insert(0, numero)
    
    if numero % 2 == 0:
        lista_pares.insert(0, numero)
    else:
        lista_impares.insert(0, numero)
    
    if escolha == 'N':
        break

print(f'A lista completa é {lista_completa}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_impares}')
