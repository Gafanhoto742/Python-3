
from random import randint
from time import sleep
computador = randint (0,10) #faz o computador sortear um número
#print('Pensei no número {}'.format(computador)) #teste do random
print ('-=-' * 20)
print ('Sou o seu computador, acabei de pensar em um número entre 0 e 10')
print ('Será que vocÊ consegue adivinhar?')
print('-=-' * 20)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? ')) #jogador tenta adivinhar
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print ('Mais... Tente novamente: ')
        elif jogador > computador:
            print ('Menos... Tente mais uma vez: ')
print('Acertou com {} tentativas, Parabéns'.format(palpite))

