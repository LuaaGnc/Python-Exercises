numeros_extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                    'seis', 'sete', 'oito', 'nove', 'dez',
                    'onze', 'doze', 'treze', 'catorze', 'quinze',
                    'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')

pergunta = int(input(f'Digite um número de 0 a 20: '))

while True:
    if 20 >=pergunta >= 0:
        break
    pergunta = int(input('Tente novamente. Digite um número de 0 a 20: '))

print(f'O número {pergunta} por extenso é {numeros_extensos[pergunta]}!')
