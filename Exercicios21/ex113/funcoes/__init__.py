from colorama import Fore, init
init(autoreset=True)


def leiaint(numero_inteiro):
    """
    :param numero_inteiro: Número inteiro digitado
    :return: int(param) else ERROR
    """
    while True:
        try:
            return int(numero_inteiro)
        except Exception:
            print(Fore.RED + 'ERRO! Digite um valor inteiro válido!')
            numero_inteiro = input('Digite novamente um número inteiro: ')


def leiafloat(numero_real):
    """
    :param numero_real: Número real digitado
    :return: float(param) else ERROR
    """
    while True:
        try:
            return float(numero_real)
        except Exception:
            print(Fore.RED + 'ERRO! Digite um número real válido!')
            numero_real = input('Digite novamente um número real: ')
