# Declaração de Variáveis / Listas / Dicionários
equipa = list()
jogador = dict()
golos = list()
total_golos = list()

while True:

    golos.clear()
    jogador.clear()
    
    total = 0
    
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    partidas = int(input(f' Quantas partidas {jogador["nome"]} jogou? '))
    
    # Conta-golos [Fica dentro de uma lista]        
    for gols in range(partidas):
        golos.append(int(input(f'Quantos golos na partida {gols + 1} ')))
    jogador['golos'] = golos[:]

    # Cálculo do Total de Golos
    for g in jogador['golos']:
        total += g
        
    total_golos.append(total)
    equipa.append(jogador.copy())
    
    escolha = str(input('Quer continuar [S/N]: ')).upper().strip()
        
    if escolha in 'N':
        print('-=' * 30)
        print('cod      nome      gols      total')
        print('-' * 60)

        for enum, i in enumerate(equipa):
            
            print(f'{enum}', end='  ')
            
            for v in i.values():
                print(f'{v}  ', end='')

            print(f' {total_golos[enum]}')
        
        break
    
while True: 
    
    # COD = Nº De Jogador
    escolha_dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    # Se 999 -> Stop
    if escolha_dados == 999:
        break
    
    if escolha_dados >= len(equipa):
        print(f'ERRO! Não existe nenhum jogador com o código de {escolha_dados}')
    else:    
        print(f' -- LEVANTAMENTO DO JOGADOR {equipa[escolha_dados]["nome"]}: ')
            
        for enum, every in enumerate(equipa[escolha_dados]["golos"]):
            print(f'     No jogo {enum + 1} fez {every} golos;')

print('>> .. PROGRAMA ENCERRANDO .. <<')
    