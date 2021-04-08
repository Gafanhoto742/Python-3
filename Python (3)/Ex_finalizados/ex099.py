'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros 
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep

def maior(* num):
    cont = maior = 0
    print('_'*60)
    print ('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='',flush=True)
        sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.\n')


maior(2, 1, 7)
maior(8, 0)
maior(4, 4, 7, 6, 2)
maior(1)
maior()