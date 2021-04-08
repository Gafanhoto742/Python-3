'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''


'''lista = []

print('Digite 5 números')
for c in range(5):
    n = int(input('Número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('O número foi adicionado no final da lista.')
    else:
        for i in range(5):
            if n <= lista[i]:
                lista.insert(i,n)
                print(f'O número foi adicionado na posição {i}.')
                break
print('-'*30)
print(lista)'''


lista = []
for c in range (0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('+'*30)
print(f'Você digitou os números {lista}')