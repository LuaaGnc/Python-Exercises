sexo = str(input('Informe seu sexo: [M/F] '))

while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).upper().strip()
print(f'Sexo {sexo} registrado com sucesso!')
