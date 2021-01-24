def escreva(texto):
    tam_string = len(texto) + 2
    
    print('~' * tam_string)
    print(f' {texto:>2}')
    print('~' * tam_string)
    
escreva('Olá, Mundo!')
escreva('Palhaçada Descomunal')
    