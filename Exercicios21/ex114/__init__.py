import socket

try:
    socket.gethostbyname('www.python.org')
except:
    print('Não foi possível efetuar a ligação')
else:
    print('ok')