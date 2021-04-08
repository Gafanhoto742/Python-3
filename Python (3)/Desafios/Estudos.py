''' Reforço de IF, ELIF e ELSE'''

from time import sleep

while True:
    pessoa = str(input('\nQual é o seu nome: ')).strip().upper()
    if pessoa == "AMANDA":
        apelido = 'Mands'
        
        print(f'{pessoa}!') 
        print('Nome Lindo hein!')
    while True:
        resp = str(input('Deseja cadastrar outro jogador? [S/N]')).strip().upper()[0]
        if resp in "SN":
            break
        print(f'[ERRO] - Digite S ou N: ')
        if resp == "N":
            break