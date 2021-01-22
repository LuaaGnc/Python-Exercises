produtos = ('Computador',500 , 'Telemóvel', 256.33,
 'Pen Drive', 49.99, 'Carregador', 15, 'HDD', 109.99)

print('-' * 40)
print(' ' * 13, 'LISTAGEM DE PREÇOS')
print('-' * 40)

for contador in range(0, len(produtos), 2): # Parentesis = alinhar à esquerda(o texto) 30 pontos
    print(f'{produtos[contador]:.<30}{produtos[contador + 1]}€')
