print('=' * 40)
print(' ' * 11, 'Loja da Filomena')
print('=' * 40)

total_gasto = produtos = 0
preco_produto_barato = 99999999999999999999999

while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço(€): '))
    escolha = str(input('Quer continuar? [S/N] ').upper().strip())
    total_gasto += preco
    print('=' * 40)
    if escolha in 'N':
            break

    elif preco >= 1000:
        produtos += 1

    elif preco_produto_barato >= preco:
        produto_barato = nome
        preco_produto_barato = preco

print('+-' * 20)
print(f'Na sua compra gastou um total de {total_gasto:.2f}€')
print(f'{produtos} artigo custa(m) mais de 1000€ sendo que o produto mais barato foi o {produto_barato} com ', end='')
print(f'o preço de {preco_produto_barato}€.')
