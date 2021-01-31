def aumentar(base, percent, formatado=False):
    # Se False --> Significa que não quer formatar então não é chamada a função moeda
    # Se True --> Significa que quer formatar então é chamada a função moeda
    # --/ --/ --> É igual para os restantes <-- \-- \--
    aumento_final = base + (base * percent/100)
    return aumento_final if formatado is False else moeda(aumento_final)


def diminuir(base, percent, formatado=False):
    diminuicao_final = base - (base * percent/100)
    return diminuicao_final if formatado is False else moeda(diminuicao_final)


def dobro(base, formatado=False):
    dobrado = base * 2
    return dobrado if formatado is False else moeda(dobrado)


def metade(base, formatado=False):
    half = base / 2
    return half if formatado is False else moeda(half)


def moeda(valor):
    valor = str(valor)
    valor = 'R$' + valor.replace('.', ',')
    return valor
