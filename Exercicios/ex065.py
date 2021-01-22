maior_valor = menor_valor = contador = soma_total = media = 0
answer = 'S'

while answer == 'S':

    numero = int(input('Digite um número: '))
    answer = str(input('Quer continuar? [S/N] ')).strip().upper()
    contador += 1
    soma_total += numero

    if maior_valor == menor_valor == 0:
        maior_valor = menor_valor = numero

    if maior_valor < numero:
        maior_valor = numero
    elif menor_valor > numero:
        menor_valor = numero

media = soma_total/contador

print(f'Você digitou {contador} números e a média foi {media}')
print(f'O maior valor foi {maior_valor} e o menor foi {menor_valor}')
