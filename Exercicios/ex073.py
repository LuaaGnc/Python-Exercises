equipas = ('Belenenses', 'Benfica', 'Boavista', 'V.Setúbal', 'Tondela',
           'Sp.Braga', 'Rio Ave', 'Portimonense', 'FC Porto', 'Sporting',
           'Paços Ferreira', 'Marítimo', 'Gil Vicente', 'Moreirense',
           'Famalicão', 'Santa Clara')

print('-=' * 40)
print(f'Lista de Equipas Portuguesas {equipas}')
print('-=' * 40)
print(f'As primeiras 5 equipas são: {equipas[:5]}')
print('-=' * 40)
print(f'Os últimos 4 são: {equipas[-4:]}')
print('-=' * 40)
print(f'Equipas em ordem alfabética: {sorted(equipas)}')
print('-=' * 40)
print(f'O Benfica está na {equipas.index("Benfica")}')  # Usar aspas duplas neste caso!!!!
