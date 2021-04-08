'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a 
listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

n = (randint(0, 20), randint(0, 20), randint(0, 20),
randint(0, 20), randint(0, 20), randint(0, 20))

print (f'Os valores sorteados foram: ', end='')

for num in n:
    print (f'{num} ', end='')
print (f'\nO maior valor sorteado foi {max(n)}')
print (f'O menor valor sorteado foi {min(n)}')