'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato 
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''


times = ('Santo André', 'Palmeiras', 'São Paulo', 'Bragantino', 'Mirassol', 
'Guarani', 'Novorizontino', 'Santos', 'Inter de Limeira', 'Corinthians',
'Ferroviaria', 'Oeste', 'Ituano', 'Água Santa', 'Botofogo-SP', 'Ponte Preta')

print ('*'*26)
print (' Campeonato Paulista 2020')
print ('*'*26)
print (f'Conheça os 5º primeiros da tabela: {times[:5]}')
print ('*'*26)
print (f'Também saiba os lanterninhas da tabela do Paulistão de 2020: {times[-5:]}')
print ('*'*26)
print (f'Você sabia que todos esses times estão participando do Paulistão de 2020? : {sorted(times)}')
print ('*'*26)
for pos, clube in enumerate(times):
    if clube == 'Corinthians':
        print (f'O Corinthians encontra-se na {pos+1}ª colocação.')


