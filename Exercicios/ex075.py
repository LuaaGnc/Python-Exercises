numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite mais outro número: '))
numero4 = int(input('Digite um último número: '))

tupla = (numero1, numero2, numero3, numero4)

print(f'O número 9 apareceu {tupla.count(9)} vez(es)')
if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index(3) + 1} º posição')
else:
    print('O número 3 não está na Tupla.') 

print(f'Os números pares foram ', end='')

for contador in tupla:
    if contador % 2 == 0:
        print(contador, end=' ')
