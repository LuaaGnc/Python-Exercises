lista_numeros = []

for contador in range(0, 5):
    numero = int(input('Digite um valor: '))

    if contador == 0 or numero > lista_numeros[-1]:
        lista_numeros.append(numero)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        
        while posicao < len(lista_numeros):
            if numero <= lista_numeros[posicao]:
                lista_numeros.inserto(posicao, numero)
                break
            posicao += 1

print('-=' * 30)
print(f'A sua lista ordenada é {lista_numeros}')
    