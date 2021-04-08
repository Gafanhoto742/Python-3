from random import randint
from time import sleep
'''
valcp = [] #lista valor computador
par = [] #lista de números pares
soma = 0

for c in range(0, 6):
    computador = randint (0,10)
    if computador not in valcp:
        valcp.append(computador)

for indice, valor in enumerate(valcp):
    if valor % 2 == 0:
        par.append(valor)
        
print('-'*60)
print(f'Sorteando 5 valores: {valcp}', end=' ')
valcp.sort()
print('<<<PRONTO>>>')

print(f'\nOs pares da lista sorteada são {par} e a soma entre eles da ', end='')
print(f'{len(par)}')


'''

def sorteia(lista):
    print('Sorteando valores da lista >>>', end=' ')
    for c in range(5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('<<< PRONTO')


def par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma +=valor

    print(f'Somando os valores pares da {lista}, {pares} temos {soma}')

números = []#lista
sorteia(números)
par(números)



'''
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))

    r = str(input('Deseja continuar: [S/N]: ')).strip().upper()[0]
    if r in 'N':
        break

for indice, valor in enumerate(lista):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    
print ('-='*30)
print (f'A lista completa é {lista}')
print (f'A lista de pares é {pares}')
print (f'A lista de ímpares é {impares}')'''