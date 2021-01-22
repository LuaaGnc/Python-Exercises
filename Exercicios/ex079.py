lista_numeros = []

while True:
    numero = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar?[S/N] ').strip().upper())

    if numero not in lista_numeros:
        lista_numeros.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    if resposta == 'N':
        break
lista_numeros.sort()
print('-=' * 30)
print(f'Tu digitaste os valores {lista_numeros}')
