
Alunos = []

while True:

    Aluno = []

    Aluno.append(str(input('Nome: ')))
    Aluno.append(int(input('Nota 1: ')))
    Aluno.append(int(input('Nota 2: ')))

    Alunos.append(Aluno)

    escolha = str(input('Quer continuar: [S/N] ')).lower().strip()

    if escolha in 'n':
        break


print('-=' * 25)
print('No. NOME         MÉDIA')

for c in range(len(Alunos)):
    media = (Alunos[c][1] + Alunos[c][2]) / 2
    print(f'{c + 1}', end=' ')
    print(f'{Alunos[c][0]}', end=' ')
    print(f'{media}')

