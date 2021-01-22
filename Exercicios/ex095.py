# Declaração de Variáveis / Listas / Dicionários
equipa = list()
jogador = dict()
golos = list()

total = 0

while True:

    golos.clear()
    jogador.clear()
    
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    partidas = int(input(f' Quantas partidas {jogador["nome"]} jogou? '))
    
    # Conta-golos [Fica dentro de uma lista]        
    for gols in range(partidas):
        golos.append(int(input(f'Quantos golos na partida {gols + 1} ')))
    jogador['golos'] = golos[:]

    # Total de Golos
    for algo in range(len(golos)):
        total += golos[algo]
        
    equipa.append(jogador.copy())
    
    escolha = str(input('Quer continuar [S/N]: ')).upper().strip()
        
    if escolha in 'N':
        break

print('-=' * 30)
print('cod    nome    gols    total')

for i in equipa:
    for v in i.values():
        print(f'{v}', end='')
    print()