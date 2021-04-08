'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos 
 digitados, em ordem crescente. '''

val=[]

while True:

    valor = int(input('Digite um valor: '))
    
    if valor not in val:
        val.append(valor)
        print('Valor adicionado com sucesso...')

    else:
        print('Valor repetido, não será adicionado a lista')


    res = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if res in 'Nn':
        break

print ('_-'*30)

print('')

val.sort()
print (f'Você digitou os valores {val}')

print ('_-'*30)

print('')

print('PROGRAMA ENCERRADO')
print('Script R1ckOl1v3r')