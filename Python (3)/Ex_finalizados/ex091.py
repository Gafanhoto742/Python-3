''' Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from operator import itemgetter

j = {'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)} 
ranking = {}

print ('Valores sorteados:')
for keys, valor in j.items():
    print(f'{keys} tirou {valor} no dado.')

print('=+'*15)

ranking = sorted(j.items(), key=itemgetter(1), reverse=True)

print(f'{"==Ranking dos Jogadores==":^30}')
for i, v in enumerate(ranking):
    
    print(f'   {i+1}º lugar: {v[0]} tirou {v[1]}')

print('=+'*15)

print('FIM DE PROGRAMA')


