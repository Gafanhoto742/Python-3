'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: OK
A) Quantos números foram digitados. - ok
B) A lista de valores, ordenada de forma decrescente. - OK
C) Se o valor 5 foi digitado e está ou não na lista.'''


val = []

while True:
    val.append(int(input('Digite um valor: ')))
    res = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if res in 'N':
        break

print('_='*30)


print(f'\nVocê digitou {len(val)} elementos.')

print(f'\nOs números digitados em ordem decrescente são: {sorted(val, reverse=True)}')

if 5 in val:
    print(f'\nO número 5 faz parte da sua lista na {val.index(5)+1}ª posição')
else:
    print('\nNão encontrei o número 5 em sua lista!')

print('')
print('_='*30)
print('\nFIM DO PROGRAMA')
print('Script R1ckOl1v3r')