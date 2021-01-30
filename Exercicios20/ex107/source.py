import moeda_func

preco = float(input('Digite o preço: R$ '))

print(f'A metade de R${preco:.2f} é R${moeda_func.metade(preco):.2f}')
print(f'O dobro de R${preco:.2f} é R${moeda_func.dobro(preco):.2f}')
print(f'Aumentando 10%, temos R${moeda_func.aumentar(preco, 10)}')
