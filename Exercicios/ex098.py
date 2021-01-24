
# Algoritmo que Imprime as contagens
def contagem(inicio, fim, passo):

    if passo > 0:
        if fim > inicio:
            for i in range(inicio, fim + 1, passo):
                print(i, end=' ')
        else:
            for i in range(inicio, fim + 1, -passo):
                print(i, end=' ')
    elif passo == 0:
        if fim > inicio: 
            for i in range(inicio, fim, 1): 
                print(i, end=' ')
        else:     
            for i in range(inicio, fim + 1, -1):
                print(i, end=' ')
    
# Falta fazer esta parte
#    elif passo < 0:
        
# print('-=' * 30)
# contagem(1, 10, 1)

# print('-=' * 30)
# contagem(10, 0, 2)    

print('Agora é a sua vez de personalizar a contagem!')

# Requisição dos parâmetros
inicio = int(input('Início: ')) 
fim = int(input('Fim:    '))
passo = int(input('Passo:   '))

# Envio dos parâmetros e Chamamento de função
contagem(inicio, fim, passo)
