def leiadinheiro(numero):
    valido = False

    while not valido:
        if numero.isalpha():
            print(f'\u001b[31m ERRO: {numero} não é um preço válido \u001b[0m')
            a = input('Digite novamente um preço: R$').replace(',', '.')
            numero = a
        else:
            valido = True
            return float(numero)
