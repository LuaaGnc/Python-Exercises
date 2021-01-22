frase = str(input('Digite uma frase: ')).upper().strip().split()
frase_junto = ''.join(frase)
frase_invertida = frase_junto[::-1]
print(f'A sua frase é {frase_junto} e o seu inverso é {frase_invertida}!')
if frase_junto == frase_invertida:
    print('A frase digitada É UM PALÍNDROMO!')
else:
    print('A frase NÃO É UM PALÍNDROMO!')
