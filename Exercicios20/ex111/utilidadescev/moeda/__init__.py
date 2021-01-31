def resumo(base, percentaumentar=0, percentdiminuir=0, formatado=False):
    """
    :param base: Redirecionado para Dobro e Metade
    :param percentaumentar: Redirecionado para Aumentar
    :param percentdiminuir: Redirecionado para Diminuir
    :return: Para os 4 acima
    """
    base_formatado = moeda(base)
    dob = dobro(base, formatado)
    met = metade(base, formatado)
    aum = aumentar(base, percentaumentar, formatado)
    dim = diminuir(base, percentdiminuir, formatado)

    print('-' * 30)
    print(' ' * 7, 'Resumo do valor')
    print('-' * 30)

    print(f'Preço analisado:    {base_formatado}')
    print(f'Dobro do preço:     {dob}')
    print(f'Metade do preço:    {met}')
    print(f'{percentaumentar}% de aumento:     {aum}')
    print(f'{percentdiminuir}% de redução:     {dim}')


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
