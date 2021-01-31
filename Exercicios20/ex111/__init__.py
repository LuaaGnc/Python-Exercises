from utilidadescev import dado
from utilidadescev import moeda

preco = dado.leiadinheiro(input('Digite o preço: R$ '))
moeda.resumo(preco, 80, 35, True)
