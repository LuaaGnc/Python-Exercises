print('=' * 33)
print(' ' * 5, '10 TERMOS DE UMA PA', ' ' * 5)
print('=' * 33)

primeiro_termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo_geral = 0
termo = 0
for contagem in range(1, 11):

    termo = primeiro_termo + (contagem - 1) * razao
    print(termo, '-> ', end='')
print('ACABOU')
