soma = contador = 0
while True:
    numero = int(input('Digite um número[999 para parar]: '))

    if numero == 999:
        break

    soma += numero
    contador += 1

print(f'Foram mostrados {contador} números e a soma entre eles foi {soma}!')
