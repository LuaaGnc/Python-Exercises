jogador = dict()
golos = list()
total = 0 

jogador['nome'] = str(input('Nome do Jogador: ')).capitalize().strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for sth in range(partidas):
    
    x = int(input(f'Quantos golos na partida {sth}? '))
    golos.append(x)
    
    total += x
     
jogador['golos'] = golos    
jogador['total'] = total
print('-=' * 30, '\n', jogador, '\n', '-=' * 30)

for k, v in jogador.items():
    print(f' O campo {k} tem o valor {v}.')

print('-=' * 30)
print(f'O Jogador {jogador["nome"]} jogou {partidas}. ')

for c, v in enumerate(jogador['golos']):
    print(f'    => Na partida {c}, fez {v} golos.')
print(f' O jogador {jogador["nome"]} fez {total} golos.')
