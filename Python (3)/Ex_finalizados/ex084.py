

banco = []
dado = []
maiorp = menorp = n = 0

print('-='*30)
print(f'\033[7;30;39m{"CADASTRO DE PESSOAS":^60}\033[m')
print('-='*30)


while True:
    n +=1
    print(f'------{n}ª PESSOA------')

    dado.append(str(input('Nome: ')))

    dado.append(int(input('Idade: ')))


    dado.append(int(input('Peso: ')))

    if len(banco) == 0:
        maiorp = menorp = dado[2]
    else:
        if dado[2] > maiorp:
            maiorp = dado[2]
        
        if dado[2] < menorp:
            menorp = dado[2]

    
    banco.append(dado[:])
    dado.clear()


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break


print('-='*30)

print(f'\nAo todo, você cadastrou {len(banco)} pessoas.')

print(f'\nO maior peso foi de {maiorp}Kg. Peso de ',end='')
for p in banco:
    if p[2] == maiorp:
        print(f'[{p[0]}]',end=' ')

print(f'\nO menor peso foi de {menorp}Kg. Peso de ', end='')
for p in banco:
    if p[2] == menorp:
        print(f'[{p[0]}]',end=' ')



