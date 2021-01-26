from time import gmtime, strftime

# Importa o ano do sistema
ano_sistema = int(strftime('%Y', gmtime()))

# Função que determina se pode ou não votar
def vota(ano_sistema, ano_nascimento):
    idade = ano_sistema - ano_nascimento

    if idade >= 18:
        print(f' --> Com {idade} anos: VOTA! ')
    else:
        print(f' --> Com {idade} anos: NÃO VOTA!')

ano_nascimento = int(input('Em que ano você nasceu? '))
vota(ano_sistema, ano_nascimento)
