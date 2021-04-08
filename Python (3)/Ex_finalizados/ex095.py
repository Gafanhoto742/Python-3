'''Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

jogador = {} 
ngols = [] # número de gols
ljogadores = [] # Lista de jogadores
soma = j = 0 

print ('='*60)
print (f'\033[7;30;39m{"CADASTRO DE JOGADOR":^60}\033[m')
print ('='*60)

while True:

    jogador.clear()

    j += 1
    jogador['Nome'] = str(input(f'Nome do {j}º Jogador: ')).strip().upper()
    npart = int(input(f'Quantas partidas que \033[2;33m{jogador ["Nome"]}\33[m participou?: ')) #numero de partidas
    ngols.clear()
    for c in range(0, npart):
        c +=1
        ngols.append(int(input(f'Quantos Gols que \033[3;33m{jogador["Nome"]}\33[m fez na {c}º partida: ')))
    jogador['Gols'] = ngols[:]
    jogador['Saldo de gols'] = sum(ngols)

    ljogadores.append(jogador.copy())
    
    print('='*60)

    while True:
        resp = str(input('Deseja cadastrar outro jogador? [S/N]')).strip().upper()[0]
        if resp in "SN":
            break
        print(f'[ERRO] - Digite S ou N: ')
    if resp == "N":
        break

print('='*60)

print ('Cód', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('='*60)

for k, v in enumerate(ljogadores):
    print(f'{k:>2}',end='  ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('='*60)

while True:
    perg = int(input('Quer saber os dados de qual jogador? [999-parar Consulta]'))
    if perg == 999:
        break
    if perg >= len(ljogadores):
        print(f'[ERRO!] - Não existe esse jogador na lista, digite um código válido {perg}')
    else:
        print(f'   \033[7;30;39m---- LEVANTAMENTO DO JOGADOR \033[3;33m{ljogadores[perg]["Nome"]}\033[m:')
        for i, g in enumerate(ljogadores[perg]['Gols']):
            print(f'   No {i+1}º jogo fez {g} gols')


print('='*60)
print(f'{"==* PROGRAMA ENCERRADO *==":^30}')

