def valida(nome, golos):
    print(f' O jogador {nome} marcou {golos_jogador} golos.')

nome_jogador = input('Qual é o nome do jogador? ').strip().capitalize()
golos_jogador = input('Número de golos? ').strip()

if golos_jogador.isnumeric():
    golos_jogador = int(golos_jogador)
else:
    golos_jogador = 0

if nome_jogador == '':
    valida('<desconhecido>', golos_jogador)
else:
    valida(nome_jogador, golos_jogador)

