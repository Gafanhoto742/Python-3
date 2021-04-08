'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.'''

from random import randint 
from time import sleep 

jogada = []
lista = []
cont = 0


print('-'*30)
print(f'{"JOGADA NA MEGA SENA":^30}')
print('-'*30)


j = int(input('Quantos jogos você quer que eu sorteie? : '))
sleep(1)





print ('*'*3, f'Sorteando {j} jogos!', '*'*3)
sleep(1)

print('-'*30)

for p in range(j):
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogada.append(lista[:])
    lista.clear()


    
    print(f'{p+1}º Jogada:{jogada}')
