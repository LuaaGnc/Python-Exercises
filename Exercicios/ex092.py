
trabalhador = dict()
 
trabalhador['nome'] = str(input('Nome: ')).capitalize().strip()
trabalhador['nascimento'] = int(input('Ano de nascimento: '))
trabalhador['carteira_trabalho'] = int(input('Carteira de Trabalho (0 - Não tem): ')) 

if trabalhador['carteira_trabalho'] != 0:
    
    trabalhador['ano_contratacao'] = int(input('Ano de Contratação: ')  )
    trabalhador['salario'] = int(input('Salário(€): '))

    trabalhador['reforma'] = 60 - (2021 - trabalhador['ano_contratacao']) 

print('-=' * 25)

for k, v in trabalhador.items():
    print(f'   - {k} tem o valor {v}')
print()
