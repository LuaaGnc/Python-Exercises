lista_lista = list()
dados_pessoais = list()
lista_pesados = list()
lista_leves = list()

pessoa = peso_maior = peso_menor = 0

while True: 
    dados_pessoais.append(str(input('Qual é o teu nome? ')))
    dados_pessoais.append(float(input('Qual o seu peso? '))) 
    question = str(input('Deseja continuar? [S/N] ').strip().upper())
    if pessoa == 1:
        peso_menor = dados_pessoais[1]
    
    lista_lista.append(dados_pessoais[:]) 
    pessoa += 1
    
    if peso_maior < dados_pessoais[1]:
        peso_maior = dados_pessoais[1]
        lista_pesados.append(dados_pessoais[0])

    if peso_menor > dados_pessoais[1]:
        peso_menor = dados_pessoais[1]
        lista_leves.append(dados_pessoais[0])

    dados_pessoais.clear()    
    
    if question == 'N':
        break

print('-=' * 30)
print(f'Ao todo, cadastraram-se {pessoa} pessoas')
print(f'O maior peso foi de {peso_maior}Kg. E foram das pessoas {lista_pesados[i::1] for i in range(1)}')
print(f'O menor peso foi de {peso_menor}Kg. E foram das pessoas {lista_leves}')
