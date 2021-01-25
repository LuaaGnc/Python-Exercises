def maior(*args):
    mai = 0
    
    print('-=' * 50)
    print('Analisando os valores passados . . . ')

    for i in range(len(args)):
       
        print(f'{args[i]}', end=' ')

        if i == 0:
            mai = args[i]
        else:
            if args[i] > mai:
             mai = args[i]


    print(f'Foram informados {len(args)} valores ao todo')
    print(f'O maior valor informado foi {mai} .')


maior(2, 9, 4, 5, 7, 1)
maior(7, 4, 0, 9, 20, 45, 20)
maior(1, -3, -4, 10, 20)
maior(6)
