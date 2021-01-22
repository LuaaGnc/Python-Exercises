multiplicador = 1

while True:
    print('-' * 70)
    numero_tabuada = int(input('Quer ver a tabuada de qual valor?[Nº negativo para Encerramento]  '))
    print('-' * 70)

    if numero_tabuada < 0:
        break

    for multiplicador in range(1, 11):
        resultado_multiplica = numero_tabuada * multiplicador
        print(f'{numero_tabuada} x {multiplicador} = {resultado_multiplica}')

print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
