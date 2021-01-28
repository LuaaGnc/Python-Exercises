def notas(*args, sit=False):
    """

    :param args: NOTAS DO ALUNO ==> Entre 0 a 20 para o bom funcionamento
    :param sit: SE sit = True, mostra a situação em que o aluno se apresenta; se não, não mostra
    :return: aluno <== Dicionário com as informações do aluno

    """

    aluno = dict()
    maior, menor, soma = 0, 0, 0
    total = len(args)
    for i in range(len(args)):
        soma += args[i]

        # Condição para detetar o MAIOR e o MENOR
        if i == 0:
            maior = args[i]
            menor = args[i]
        elif i != 0 and args[i] > maior:
            maior = args[i]
        elif i != 0 and args[i] < menor:
            menor = args[i]

    media = soma/total

    aluno['total'] = total
    aluno['maior'] = maior
    aluno['menor'] = menor
    aluno['media'] = media

    # Escolhe se quer ou não mostrar a situação
    if sit:
        if 0 < media < 10:
            situacao = 'RECUPERAÇÃO'
        elif media <= 15:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'EXCELENTE'

        aluno['sit'] = situacao

    return aluno

resp = notas(1, 2, 3, 20, 5, 8, 18, 17, 15, sit=True)
print(resp)