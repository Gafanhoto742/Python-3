'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve 
perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

soma = media = maior = menor = cont = 0
res = 'S'
while res in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    res = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]


print('Você digitou {} a soma entre os valores {} e a média entre eles foi {:.1f} '.format(cont, soma, media))
print('Maior número foi {} e o menor foi {}'.format(maior, menor))