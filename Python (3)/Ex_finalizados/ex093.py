'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
 quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
  incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
ngols = []
soma = 0

print ('='*60)
print (f'{"CADASTRO DE JOGADOR":^60}')
print ('='*60)


jogador['nome'] = str(input('Nome do Jogador: ')).strip()
npart = int(input(f'Quantas partidas que {jogador ["nome"]} participou?: ')) #numero de partidas
for c in range(0, npart):
    c +=1
    ngols.append(int(input(f'Quantos Gols que {jogador["nome"]} fez na {c}º partida: ')))
jogador['gols'] = ngols[:]
jogador['tot'] = sum(ngols)

print('='*60)
        
print('='*60)
print(jogador)
print('='*60)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('='*60)

print(f'O jogador {jogador["nome"]} particiou de {npart} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'    =>Na partida {i+1}º, fez {v} Gols.')
print(f'Foi o total de {jogador["tot"]} gols')

print('='*60)
print(f'{"PROGRAMA ENCERRADO":^30}')
print('='*60)
