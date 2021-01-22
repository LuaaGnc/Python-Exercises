from random import randint
from time import sleep

print('-' * 25)
print('       EuroMilhões')
print('-' * 25)

# Declaração de Constantes
n = 0
lista_numeros = []
lista_estrelas = [] 
lista_n = []
lista_e = []

numero_jogos = int(input('Quantos jogos quer jogar? -> '))
print('\n\n')

# Lista Números 
for cn in range(1, 51):
    lista_numeros.append(cn)
    
# Lista Estrelas
for ce in range(1, 13):
    lista_estrelas.append(ce)

# Determina a quantidade de "jogos" que jogamos
while numero_jogos != 0:
    
    # Escolha aleatória dos números
    for num in range(5):
        lista_n.append(randint(lista_numeros[0], lista_numeros[-1]))
    lista_n.sort()

    # Escolha aleatória das estrelas
    for est in range(2):
        lista_e.append(randint(lista_estrelas[0], lista_estrelas[-1]))
    lista_e.sort()
    
    # .clear() Remove todos os itens de uma lista
    
    n += 1 
    print(f'       [ Jogo {n} ]')
    
    print(f'Números:  {lista_n[:]}')
    print(f'Estrelas: {lista_e[:]}\n')
    
    lista_n.clear()
    lista_e.clear()
    
    sleep(1)
    numero_jogos -= 1

print('-=-=-=-=- Good Luck My Friend! -=-=-=-=-\n')
