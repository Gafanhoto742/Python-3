'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. '''

from time import sleep
num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
op = 0
print ('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
while op != 5:
    op = int(input('>>>> Qual é a sua opção: '))
    if op == 1:
        res = num1 + num2 
        print ('A soma entre {} e {} é igual = {}'.format(num1, num2, res))
    elif op == 2:
        res = num1 * num2
        print('A multiplicação entre {} e {} = {}'.format(num1 ,num2 , res))
    elif op == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior número entre {} e {} é {}'.format(num1, num2, maior))
    elif op == 4 :
        print('Informe os números novamente:')
        num1 = int(input('Digite o 1º valor: '))
        num2 = int(input('Digite o 2º valor: '))
    elif op == 5:
        sleep(1)
        print('Finalizando....')
    else:
        print('Opção inválida. Tente novamente')
    print ('=-='*10)
sleep(1)
print ('Fim do programa! Volte sempre')


