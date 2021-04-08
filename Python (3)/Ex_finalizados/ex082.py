'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

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
print (f'A lista de ímpares é {impares}')
