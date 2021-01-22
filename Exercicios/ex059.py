from time import sleep

option = 0

primeiro_valor = int(input('Primeiro valor inteiro: '))
segundo_valor = int(input('Segundo valor inteiro: '))

while option != 5:

    print(' [ 1 ] SOMAR \n [ 2 ] MULTIPLICAR \n [ 3 ] MAIOR')
    print(' [ 4 ] NOVOS NÚMEROS \n [ 5 ] SAIR DO PROGRAMA')
    option = int(input('>>>>> Qual é a sua opção? '))

    if option == 1:
        valor_mostrado = primeiro_valor + segundo_valor
        print(f'A soma entre {primeiro_valor} + {segundo_valor} é {valor_mostrado}!')

    elif option == 2:
        valor_mostrado = primeiro_valor * segundo_valor
        print(f'O resultado de {primeiro_valor} x {segundo_valor} é {valor_mostrado}!')

    elif option == 3:
        if primeiro_valor > segundo_valor:
            print(f'O maior valor entre {primeiro_valor} e {segundo_valor} é {primeiro_valor}!')
        elif primeiro_valor < segundo_valor:
            print(f'O maior valor entre {primeiro_valor} e {segundo_valor} é {segundo_valor}!')
        elif primeiro_valor == segundo_valor:
            print(f'Os valores {primeiro_valor} e {segundo_valor} são iguais!')

    elif option == 4:
        print('--> Informe os números novamente <--')
        primeiro_valor = int(input('Primeiro valor inteiro: '))
        segundo_valor = int(input('Segundo valor inteiro: '))

    elif option not in [1, 2, 3, 4, 5]:
        print('Opção inválida. Tente novamente!')

    print('=-=' * 10)
    sleep(2)

print('Finalizando...')
print('=-=' * 10)
sleep(4)
print('Fim do programa! Volte sempre!!!')
