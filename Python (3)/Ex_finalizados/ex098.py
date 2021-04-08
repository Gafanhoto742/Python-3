'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada '''

from time import sleep

def cont(inic, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0 :
        passo = 1
    print('~'*30)
    print(f'Contagem de {inic} até {fim} de {passo} em {passo}')
    sleep(0.5)

    if inic < fim:
        c = inic
        while c <= fim:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c += passo
        print('  <<< FIM')

    else:
        c = inic
        while c >= fim:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c -= passo
        print('  <<< FIM')

#principal
cont (1 , 10, 1)
cont (10, 1 , 2)
print('~'*30)
print('Agora a sua vez de personalzar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
cont (i, f, p)


  
   


