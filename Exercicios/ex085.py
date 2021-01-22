# Separa os números Pares e os Ímpares

lista_pares = []
lista_impares = []

for c in range(1, 8):
    numero = int(input(f'Digite o {c}o. número: '))

    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero) 

lista_pares.sort()
lista_impares.sort()
print('-=' * 30)
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares {lista_impares}')
