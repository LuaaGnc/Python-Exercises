pessoa_maior = 0
pessoa_menor = 0
for i in range(1, 8):
    ano_pessoa = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    if ano_pessoa <= 1900 or ano_pessoa >= 2021:
        print('Your not alive bitch!')
        break
    elif ano_pessoa <= 2002:
        pessoa_maior += 1
    else:
        pessoa_menor += 1
print(f'\n Ao todo tivemos {pessoa_maior} pessoas maior de idade.')
print(f' E também tivemos {pessoa_menor} pessoas menores de idade.')
