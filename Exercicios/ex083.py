expressao = str(input('Digite uma expressão: '))

esquerda = expressao.count('(')
direita = expressao.count(')')

print('A expressão está ', end='')
if esquerda == direita:
    print('correta!')
else:
    print('incorreta!')
