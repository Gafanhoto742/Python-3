'''cont = 1
while cont <= 10:
    print(cont, '->', end='')
    cont += 1
print('Acabou')

n = s = 0
while True: #estrutura de repetição infinita, com pausa ao chegar no Break = 999
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print ('A soma vale {}'.format(s))

n = s = cont = 0
while True: # estrutura de repetição infinita e soma de contadores
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
    cont += 1
print('Você digitou {} números e a soma entre eles vale {}'.format(cont, s))
'''
num = soma = cont = maior = menor = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Você digitou {cont} números e a soma entre eles vale {soma}')
print(f'E o maior número digitado foi {maior} e o menor foi {menor}')

'''
#dica para nova escrita de Python Fstring
nome = 'Zoreia'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}.')
'''