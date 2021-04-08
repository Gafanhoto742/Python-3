'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer 
como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~


def tit(txt):
    print('~'*60)
    print(txt)
    print('~'*60)


tit(f'{"Olá Mundo!":^60}')
tit(f'{"<<<Hoje foi tenso, mas consegue fazer!>>>":^60}')
tit(f'{"Henrique Oliveira":^60}')
tit(f'{"CORINTHIANS!":^60}')

'''

#Dica Guanabara
def tit(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


tit(f'{"Olá Mundo!"}')
tit(f'{"Henrique Oliveira"}')
tit(f'{"CORINTHIANS!"}')
