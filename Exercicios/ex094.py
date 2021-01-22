turma = list()
aluno = dict()
mulheres = list()

idades = 0

while True: 
    
    aluno['nome'] = str(input('Nome: ')).capitalize().strip()
    aluno['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    
    # Verificação de Sexo introduzido corretamente
    if aluno['sexo'] not in 'MF':
        print('ERRO! Responda apenas com M ou F')
        aluno['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    
    if aluno['sexo'] == 'F':
        mulheres.append(aluno['nome'])
        
    aluno['idade'] = int(input('Idade: '))
    idades += aluno['idade']
    
    turma.append(aluno.copy())
        
    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
    
    # Verificação de Escolha introduzida corretamente
    if escolha not in 'SN':
        print('ERRO! Responda apenas com S ou N')
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
        
    elif escolha in 'N':
        break

media_idades = idades/len(turma)
    
print('-=' * 30)
print(f'A) Ao todo temos {len(turma)} pessoas cadastradas.')    
print(f'B) A média de idades é de {media_idades:.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
# Imprime quem tem o sexo Feminino denotado
for k in turma:
    if k['sexo'] in 'F':
        print(f' {k["nome"]}  ', end=' ')

print()

for l in turma:
    if l['idade'] > media_idades:
        for k, v in l.items():
            print(f' {k} = {v}; ', end='')

print('<< ENCERRADO >>')
