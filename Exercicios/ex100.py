from time import sleep

def soma_pares(*args):
    soma = 0
    lista_valores = list()
    print(f'Sorteando os {len(args)} valores da lista: ', end='')

    for i in range(len(args)):
        print(args[i], end=' ')
        sleep(0.3)

        lista_valores.append(args[i])

        if args[i] % 2 == 0:
            soma += args[i]

    print('PRONTO!')
    print(f'Somando os valores pares de {lista_valores}, temos {soma}')

soma_pares(5, 7, 9, 10, 5, 8, 20)