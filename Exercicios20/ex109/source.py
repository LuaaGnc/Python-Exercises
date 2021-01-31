import moeda_func

preco = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda_func.moeda(preco)} é {moeda_func.metade(preco)}')
print(f'O dobro de {moeda_func.moeda(preco)} é {moeda_func.dobro(preco)}')
print(f'Aumentando 10%, temos {moeda_func.aumentar(preco, 10, True)}')
