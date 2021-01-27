from colorama import Fore, init
init(autoreset=True)

def validaNumero(numero):
    numero_real = input(numero)
    
    while True: 
        
        if numero_real.isnumeric():
            return int(numero_real)
            break
        else:
            print(Fore.RED + 'ERRO! Digite um número válido!')
            numero_real = input(numero)

n = validaNumero('Digite um número: ')
print(f' Você acabou de digitar o número {n}')
