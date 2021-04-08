#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maiorp = 0
menorp = 0
for p in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print(' O MAIOR peso é {}Kg e o MENOR peso é {}Kg'.format(maiorp, menorp))



