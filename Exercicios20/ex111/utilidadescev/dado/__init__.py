def leiadinheiro(numero):
    valido = False

    while not valido:
        entrada = str(numero).replace(',', '.').strip()

        if entrada.isalpha() or entrada.strip() == '':
            print(f'\u001b[31m ERRO: {entrada} não é um preço válido \u001b[0m', end='')
            numero = input('  Digite novamente abaixo\n   ')
        else:
            valido = True
            return float(entrada)
