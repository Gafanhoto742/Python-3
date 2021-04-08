'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.'''

'''def ficha(jog='<Desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeonato')



nome = str(input('Nome do Jogador: '))
gols = str(input('Quantidade de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome,gols)


'''
def ficha(n='<<DESCONHECIDO>>', gol=0):
    print(f'O jogador {n} fez {gol} gol(s) no campeonato:')


#principal
nome = str(input('Nome: '))
gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)

