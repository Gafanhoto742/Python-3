'''Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''
nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}' .format('SILVA' in nome.upper()))

#in é um operador, não é um metodo.