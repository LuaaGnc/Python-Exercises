print('Gerador de PA')
print('-=' * 15)

primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
contador_termos = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador_termos <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        contador_termos += 1
    print('PAUSA')
    mais = int(input('Quantos termos queres mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados!')
