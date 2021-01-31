def aumentar(base, percent):
    aumento_final = base + (base * percent/100)
    return aumento_final


def diminuir(base, percent):
    diminuicao_final = base - (base * percent/100)
    return diminuicao_final


def dobro(base):
    dobrado = base * 2
    return dobrado


def metade(base):
    half = base / 2
    return half


def moeda(valor):
    valor = str(valor)
    valor = 'R$' + valor.replace('.', ',')
    return valor
