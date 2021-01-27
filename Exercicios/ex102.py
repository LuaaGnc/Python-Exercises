def fatorial(numero, show=False):
    fator = 1
    for number in range(numero, 0, -1):
        fator *= number
        if show and number > 1:
            print(f'{number}', end=' x ')
        if show and number == 1:
            print(f'{number} = ', end='')

    return fator

print('-' * 40)
print(fatorial(5, True))
