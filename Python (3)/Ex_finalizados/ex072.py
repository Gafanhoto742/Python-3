'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
'Dezeseis', 'Desessete', 'Dezoito', 'Dezenove', 'Vinte')
res = 'S'

while res == 'S':
    n = int(input('Digite um número de 0 a 20: '))

    if not 0 <= n <= 20:
        break

    print(f'Você digitou o número {num[n]}')
    res = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
