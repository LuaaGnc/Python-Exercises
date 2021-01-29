
def ajuda(escolha):
    help(escolha)


escolha = str(input('\u001b[42m Função ou Biblioteca:\u001b[43m'))

print('')
ajuda(escolha)
print()
while escolha != 'fim':
    escolha = str(input('\u001b[42m Função ou Biblioteca:\u001b[43m'))

    print('\u001b[41m')
    ajuda(escolha)
    print('\u001b')

print(' ~~~~~~~~~ ')
print(' ATÉ LOGO  ')
print(' ~~~~~~~~~ ')
