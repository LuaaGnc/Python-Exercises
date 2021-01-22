from random import randint
from time import sleep
from operator import itemgetter

jogador = dict()
Ranking = dict()

jogador['jogador1'] = randint(1, 6)
jogador['jogador2'] = randint(1, 6)
jogador['jogador3'] = randint(1, 6)
jogador['jogador4'] = randint(1, 6)

print('Valores sorteados: ')

for keys, values in jogador.items():
    
    print(f' O {keys} tirou {values} no dado.')
    sleep(0.5)
print()

# Cria uma Lista --> Sorteia os itens pelo 22222222 argumento ou o VALOR no caso
# e como ela é sorteada por ordem crescente,," reverse=True "
Ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

print('-=' * 25, '\n == RANKING DOS JOGADORES ==')

for indice, valores in enumerate(Ranking):
    print(f'    {indice + 1}º lugar: ', end= '')
    print(f'{valores[0]} com {valores[1]}. ')
    sleep(1)
