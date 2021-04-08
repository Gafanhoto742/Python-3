from random import randint
from time import sleep
itens = ('Pedra' , 'Papel' , 'Tesoura')
computador = randint (0,2)
print ('''Vamos jogar JO KEN PO ?
Escolha a sua opção:
[0] Pedra
[1] Papel
[2] Tesoura ''')
jogada = int(input('Qual é a sua jogada: '))
if jogada >=3:
    print('[ERRO]')
elif jogada <= 2:
    sleep (1)
    print ('JO')
    sleep (1)
    print ('KEN')
    sleep (1)
    print ('PO!!!')
    sleep (1)
    print ('-=-' * 10)
    sleep (1)
    print ('O computador escolheu {}'.format(itens[computador]))
    print ('O Jogador jogou {}'.format(itens[jogada]))
    print ('-=-' * 10)
else:
    print ('ESCOLHA UMA OPÇÃO VALIDA')
if computador == 0: #jogou pedra
    if jogada == 0 :
        print('EMPATE, TENTE NOVAMENTE!')
    elif jogada == 1 :
        print ('Parabéns, você GANHOU!')
    elif jogada == 2 :
        print ('O Computador ganhou! Boa sorte na proxima!')    
    else:
        print ('JOGADA INVÁLIDA!')
elif computador == 1 : #jogou papel
    if jogada == 0:
        print ('O Computador ganhou! Boa sorte na proxima!')
    elif jogada == 1 :
        print ('EMPATE, TENTE NOVAMENTE!')
    elif jogada == 2 :
        print ('Parabéns, você GANHOU!')
    else:
        print ('JOGADA INVÁLIDA!')
elif computador == 2 :  #jogou tesoura 
    if jogada == 0:
        print ('Parabéns, você GANHOU!')
    elif jogada == 1 :
        print ('O Computador ganhou! Boa sorte na proxima!')
    elif jogada == 2 :
        ('EMPATE, TENTE NOVAMENTE!')
    else:
        print ('JOGADA INVÁLIDA!')

