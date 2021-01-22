print('Gerador de PA')
print('-=' * 15)

primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
termo = primeiro_termo
contador_termos = 0

while contador_termos < 10:
    print(f'{termo} -> ', end='')
    termo += razao
    contador_termos += 1

print('FIM!')
