'''Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

#forma que escrevi
valor = int(input('Entre com um número para saber o fatorial: '))
fatorial = 1
while (valor>1):
    fatorial += valor
    valor -= 1
print('O fatorial de {} é {}.'.format(valor,fatorial))

# como professor montou
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))


'''
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print ('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if  c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))