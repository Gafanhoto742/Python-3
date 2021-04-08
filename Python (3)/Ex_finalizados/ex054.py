'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for d in range (1,8):
    nasc = int(input('Digite que ano a {}ª pessoa nasceu: '.format(d)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1 
print ('Ao todo tivemos {} que atingiram a maior idade:'.format(totmaior))
print ('E também tivemos {} pessoas menor de idade'.format(totmenor))
