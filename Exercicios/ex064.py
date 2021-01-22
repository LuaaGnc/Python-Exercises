numero = contador = soma = 0

while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    soma += numero
    contador += 1

print(f'Você digitou {contador - 1} números e a sua soma entre eles foi {soma - numero}.')
