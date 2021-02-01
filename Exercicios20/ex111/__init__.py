from utilidadescev import dado, moeda

preco = dado.leiadinheiro(input('Digite o preço: R$ '))
moeda.resumo(preco, 80, 35, True)
