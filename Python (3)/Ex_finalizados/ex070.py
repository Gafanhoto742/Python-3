'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
 continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''
tot = bar = mil = 0
print('-'*30)
print('{: ^30}'.format('Lojas SONOS'))
print('-'*30)
pro = None
while True:
    prod = str(input('Nome do Produto: ')).strip()
    pre = float(input('Preço: R$ '))
    tot += pre
    resp = ' '
    if pro == None or pre < bar:
        bar = pre
        pro = prod
    if pre > 1000:
        mil += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^30}'.format(' FIM DA COMPRA '))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {mil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {pro} que custa R${bar:.2f}')