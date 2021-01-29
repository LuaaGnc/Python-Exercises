from time import sleep

cores = ('\033[m',              # 0 - Sem cores
         '\033[0;30;41m',       # 1 - vermelho
         '\033[0;30;42m',       # 2 - Verde
         '\033[0;30;43m',       # 3 - Amarelo
         '\033[0;30;44m',       # 4 - Azul
         '\033[0;30;45m',       # 5 - Roxo
         '\033[7;30m')          # 6 - Branco


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[6], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(cores[0], end='')
    sleep(1)


comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = input('Função ou Biblioteca > ')

    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO!', 1)
