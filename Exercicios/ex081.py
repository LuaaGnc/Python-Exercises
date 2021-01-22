lista_numeros = []

while True:
    numeros = int(input('Digite um número: '))
    escolha = str(input('Quer continuar? [S/N]'))

    lista_numeros.insert(0, numeros)

    if escolha in 'Nn':
        break

print('-=' * 30)
lista_numeros.sort(reverse=True)
print(f'Tu digitaste {len(lista_numeros)} elementos.')
print(f'Os valores em ordem decrescente são --> {lista_numeros}')


if 5 in lista_numeros:
    print('O valor 5 faz parte da tua lista')
else:
    print('O valor 5 não está contido nessa lista')
