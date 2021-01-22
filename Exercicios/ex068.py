from random import randint

print('-=' * 25)
print('Jogo do PAR ou ÍMPAR')

vezes_jogadas = usuario_ganha = 0

while vezes_jogadas != 2:
    vezes_jogadas += 1
    print('-=' * 25)
    numero_usuario = int(input("Digite um valor: "))
    numero_computador = randint(1, 10)
    escolha_usuario = str(input('PAR ou ÍMPAR? [P/I] ').strip().upper())
    soma = numero_usuario + numero_computador
    print('-' * 50)

    if escolha_usuario != 'P' and escolha_usuario != 'I':
        print('\n\nRECOMECE NOVAMENTE E DIGITE [P] OU [I]')
        break

    elif escolha_usuario == 'P':
        if soma % 2 == 0:
            tipo = 'PAR'
            resultado = 'GANHASTE'
            usuario_ganha += 1
            print(f'Tu escolheste {numero_usuario} e o computador {numero_computador}. Total de {soma}, DEU {tipo}.')
            print('-' * 50)
            print(f'Tu {resultado}!!')
        elif soma % 2 != 0:
            tipo = 'ÍMPAR'
            resultado = 'PERDESTE'
            print(f'Tu escolheste {numero_usuario} e o computador {numero_computador}. Total de {soma}, DEU {tipo}.')
            print('-' * 50)
            print(f'Tu {resultado}!!')

    elif escolha_usuario == 'I':
        if soma % 2 != 0:
            tipo = 'ÍMPAR'
            resultado = 'GANHASTE'
            usuario_ganha += 1
            print(f'Tu escolheste {numero_usuario} e o computador {numero_computador}. Total de {soma}, DEU {tipo}.')
            print('-' * 50)
            print(f'Tu {resultado}!!')
        elif soma % 2 == 0:
            tipo = 'PAR'
            resultado = 'PERDESTE'
            print(f'Tu escolheste {numero_usuario} e o computador {numero_computador}. Total de {soma}, DEU {tipo}.')
            print('-' * 50)
            print(f'Tu {resultado}!!')

print('-=' * 25, f'\nGAME OVER! Tu ganhaste {usuario_ganha} vez(es).')
