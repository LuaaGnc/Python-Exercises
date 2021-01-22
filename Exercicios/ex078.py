pos = maior = menor = 0
lista_numeros = []
maior = menor = 0 

for v in range(0, 5):
    lista_numeros.append(int(input(f'Digite um número para a posição {pos}:')))
    
    if v == 0: 
        maior = menor = lista_numeros[v]
    else:
        if lista_numeros[v] > maior:
            maior = lista_numeros[v]
        if lista_numeros[v] < menor:
            menor = lista_numeros[v]

print('=-' * 30)
print(f'Tu digitaste os valores {lista_numeros}')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, c in enumerate(lista_numeros):
    if c == maior:
        print(f'{i}... ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, c in enumerate(lista_numeros):
    if c == menor:
        print(f'{i}... ', end='')
