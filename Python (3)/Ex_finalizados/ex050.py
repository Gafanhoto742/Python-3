'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.'''

s = 0
cont = 0
for c in range (1,7):
    n = int(input('Digite o {}º um número: '.format(c)))
    if n % 2 == 0:
        cont = cont + 1
        s = s + n
print ('Foram digitados {} números Pares e a soma dos números pares foram {}'.format(cont,s))
