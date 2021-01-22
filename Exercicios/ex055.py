peso_maior = 0
peso_menor = 0
for i in range(1, 6):
    peso_pessoa = float(input(f'Peso da {i}ª pessoa em Kg: '))
    if i == 1:
        peso_maior = peso_pessoa
        peso_menor = peso_pessoa
    else:
        if peso_pessoa > peso_maior:
            peso_maior = peso_pessoa
        if peso_pessoa < peso_menor:
            peso_menor = peso_pessoa
print(f'O peso maior lido foi de {peso_maior}Kg!')
print(f'O peso menor lido foi de {peso_menor}Kg!')
