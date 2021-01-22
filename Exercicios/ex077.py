tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for contador in tupla:
    print(f'\nNa palavra {contador} temos as letras ', end='')
    
    for letra in contador: 
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
