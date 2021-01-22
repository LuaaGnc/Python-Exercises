import random

numero_pensado = random.randint(0, 10)
numero_client = -1
contador = 0

print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? \n')

while numero_pensado != numero_client:
    numero_client = int(input('Qual é o seu palpite? '))
    if numero_pensado > numero_client:
        print('Mais... Tente mais uma vez!')
    elif numero_pensado < numero_client:
        print('Menos... Tente mais uma vez!')
    contador += 1

print(f'Acertaste à {contador}ª tentativas. Parabéns!')