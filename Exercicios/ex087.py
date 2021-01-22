# Matriz -- 3 x 3

linha1 = []
linha2 = []
linha3 = []

m1 = m2 = m3 = 0
soma_coluna3 = soma_pares = 0 
maior_valor2 = 0


for c in range(1, 10):
    
    if c in (1, 2, 3):
        numeros_linha1 = int(input(f'Digite um número para [0, {m1}]: ')) 
        m1 += 1
        linha1.append(numeros_linha1)

        if numeros_linha1 % 2 == 0:
            soma_pares += numeros_linha1
        if c == 3:
            soma_coluna3 += numeros_linha1  

    elif c in (4, 5, 6):
        numeros_linha2 = int(input(f'Digite um valor para [1, {m2}]: '))
        m2 += 1
        linha2.append(numeros_linha2)

        if numeros_linha2 % 2 == 0:
            soma_pares += numeros_linha2
        if c == 6:
            soma_coluna3 += numeros_linha2
        if maior_valor2 < numeros_linha2:
            maior_valor2 = numeros_linha2

    elif c in (7, 8, 9):
        numeros_linha3 = int(input(f'Digite um valor para [2, {m3}]: '))    
        m3 += 1
        linha3.append(numeros_linha3)

        if numeros_linha3 % 2 == 0:
            soma_pares += numeros_linha3
        if c == 9:
            soma_coluna3 += numeros_linha3

print('-=' * 25)
# Pode ser feito com -> array[0] ou 1; ou até valor -> m1 <-; 
print(f'[ {linha1[0]} ] [ {linha1[1]} ] [ {linha1[2]} ]')
print(f'[ {linha2[0]} ] [ {linha2[1]} ] [ {linha2[2]} ]')
print(f'[ {linha3[0]} ] [ {linha3[1]} ] [ {linha3[2]} ]')
print('-=' * 25)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_coluna3}')
print(f'O maior valor da segunda linha é {maior_valor2}')
