from time import sleep

def contador(inicio, fim, passo):
    
    if passo < 0 :
        passo *= -1
    if passo == 0:
        p = 1
    
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    sleep(1.5)
    
    if inicio < fim:
        cont = inicio
        
        # Enquanto o Contador(que é o início,) não for igual ao fim, adiciona ao contador "Passo".
        # Quando chegar ao "Fim" ele para(como esperado)
        while cont <= fim: 
            print(f'{cont} ', end='')
            sleep(0.2)
            cont += passo
        print('Fim!')
    
    else: 
        cont = inicio
        
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.2)
            cont -= passo
        print('Fim!')

contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
        
    