def fatorial(numero): 
    """
    :param numero: N
    :return: N Factorial
    """

    fatorial = 1
    for i in range(1, numero+1):
        fatorial *= i
    return fatorial
