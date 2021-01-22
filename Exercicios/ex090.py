aluno = dict()

aluno['nome'] = str(input('Nome: ')).capitalize()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if 0 < aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'        
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
elif 7 <= aluno['media'] <= 10:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'IMPOSSÍVEL DE DETERMINAR VISTO A UMA MÉDIA ERRADA'

for chaves, valores in aluno.items():
    print(f'   - {chaves} é igual a {valores}')
    