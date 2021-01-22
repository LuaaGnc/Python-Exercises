print('=' * 30)
print('CADASTRAR-SE')
print('=' * 30)

mulher_20 = homem = cadastro = pessoa_18 = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').upper().strip())
    escolha = str(input('Quer continuar? [S/N] ').upper().strip())
    cadastro += 1
    if sexo != 'M' and sexo != 'F'  or idade < 0 or idade > 110 or escolha == 'N':
        break

    elif sexo == 'M':
        if idade > 18:
            homem += 1
            pessoa_18 += 1
        else:
            homem += 1

    elif sexo == 'F':
        if idade <= 20:
            pessoa_18 += 1
            mulher_20 += 1
        elif idade == 18:
            mulher_20 += 1
            pessoa_18 += 1
        elif idade > 18:
            pessoa_18 += 1
    print('=' * 30)

print(f'Segundo as {cadastro} pessoas cadastradas: ')
print(f'{pessoa_18} tem mais de 18 anos \n{homem} homens se cadastraram\n{mulher_20} mulher(es) possuem menos de 20 anos')
