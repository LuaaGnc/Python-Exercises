from time import gmtime, strftime

# Importa o ano do sistema
ano_sistema = int(strftime('%Y', gmtime()))
idade = 0

# Função que determina se pode ou não votar
def vota(ano_sistema, ano_nascimento ):
    global idade
    idade = ano_sistema - ano_nascimento

    if idade >= 18:
        return True
    else:
        return False

ano_nascimento = int(input('Em que ano você nasceu? '))
resposta = vota(ano_sistema, ano_nascimento)
if resposta:
    print(f'Com {idade}: VOTA!')
else:
    print(f'Com {idade}: NÃO VOTA!')
