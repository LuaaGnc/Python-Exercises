numero = int(input('Digite um número: '))
contagem = 0
dividido = 0

for vezes in range(1, numero + 1):
    if numero % vezes == 0:
        print('\033[32m', end='')
        dividido += 1
    else:
        print('\033[31m', end='')
    contagem += 1
    print(f'{contagem}', end=' ')
print(f'\n\033[m ->O número {numero} foi divisivel {dividido} vezes!')

if  dividido == 2:
    print(f' ---> Logo, ele É PRIMO!')
else:
    print(f' ---> Logo, ele NÃO É PRIMO!')
