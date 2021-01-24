from time import sleep
# Algoritmo que Imprime as contagens
def contagem(inicio, fim, passo):

    if passo > 0:
        if fim > inicio:
            for i in range(inicio, fim + 1, passo):
                print(i, end=' ')
                sleep(0.1)
        else:
            for i in range(inicio, fim - 1, -passo):
                print(i, end=' ')
                sleep(0.1)
    
    elif passo == 0:
        if fim > inicio: 
            for i in range(inicio, fim + 1, 1): 
                print(i, end=' ')
                sleep(0.1)

        else:     
            for i in range(inicio, fim - 1, -1):
                print(i, end=' ')
                sleep(0.1)

    elif passo < 0:
        # Negativo pois Passo = +- 1
        if fim > inicio:
            for i in range(inicio, fim + 1, -passo):
                print(i, end=' ')
                sleep(0.1)

        else: 
            for i in range(inicio, fim - 1, passo):
                print(i, end=' ')
                sleep(0.1)
        
        
print('-=' * 30)
print('Contagem de 1 até 10 de 1 em 1')
contagem(1, 10, 1)
print('FIM')

print('-=' * 30)
print('Contagem de 10 até 0 de 2 em 2')
contagem(10, 0, 2)    
print('FIM')

print('Agora é a sua vez de personalizar a contagem!')

# Requisição dos parâmetros
inicio = int(input('Início: ')) 
fim = int(input('Fim:    '))
passo = int(input('Passo:   '))

# Envio dos parâmetros e Chamamento de função
contagem(inicio, fim, passo)
print('FIM')
