from random import randint

# Também poderia ter escolhido esta opção:
# tupla = ( randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10) )

primeiro_numero = randint(1, 10)
segundo_numero = randint(1, 10)
terceiro_numero = randint(1, 10)
quarto_numero = randint(1, 10)
quinto_numero = randint(1, 10)


tupla_numeros = (primeiro_numero, segundo_numero, terceiro_numero, quarto_numero, quinto_numero)
numeros_ordenados = sorted(tupla_numeros)
print(f'Os números que foram listados foram {tupla_numeros}!')
print(f'O menor número é {numeros_ordenados[0]} e o maior número é {numeros_ordenados[-1]}!')
