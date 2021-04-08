# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''
#como eu escrevi a proposta
nomep = str(input('Qual é o seu nome?' ))
print ('é um grande prazer em te conhecer {}!'.format(nomep))
n = int(input('Eu gostaria de fazer uma brincadeira de adivinhação, tente adivinhar o número que pensei entre 0 a 5 !' ))
if n == 2:
    print('Acertou, VOCÊ VENCEU!!!!!!')
else:
    print('Errouuuuuuuuuuu criança feliz, EU VENCI!!!!!!!!!')
'''

#como o professor escreveu
from random import randint
from time import sleep
computador = randint (0,5) #faz o computador sortear um número
#print('Pensei no número {}'.format(computador)) #teste do random
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
sleep(2)
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! VOCê CONSEGUIU ME VENCER!!!')
else:
    print('GANHEIIIIII !!! Eu pensei no número {} e não no {}!'.format(computador,jogador))


