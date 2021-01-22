print('=' * 40)
print(' ' * 13, 'MULTIBANCO')
print('=' * 40)

# Pergunta
valor_pedido = int(input('Quanto dinheiro pretende retirar? R$ '))

# Variáveis
notas_50 = notas_20 = notas_10 = notas_1 = 0

for c in range(0, 1):
    numero_notas50 = valor_pedido // 50

    valor_para_20 = valor_pedido - (numero_notas50 * 50)
    numero_notas20 = valor_para_20 // 20

    valor_para_10 = valor_para_20 - (numero_notas20 * 20)
    numero_notas10 = valor_para_10 // 10

    valor_para_1 = valor_para_10 - (numero_notas10 * 10)
    numero_notas1 = valor_para_1

    print(f'Total de {numero_notas50} nota(s) de 50 R$!')
    print(f'Total de {numero_notas20} nota(s) de 20 R$!')
    print(f'Total de {numero_notas10} nota(s) de 10 R$!')
    print(f'Total de {numero_notas1} nota(s) de 1 R$!')

print('=' * 40)
print('Volte sempre a este MULTIBANCO! Tenha um bom dia!')
