ano = int(input('Qual ano de fabricação do seu carro? '))
tempo = 2020 - ano
print('O seu carro tem {} anos'.format(tempo))
if tempo <=3:
    print('Carro Novo')
else:
    print('Carro velho' )
print('--FIM--')

tempox = int(input('Quantos anos tem seu carro?'))
print('Carro Novo'if tempox<=3 else'Carro Velho')
print ('--FIM--')
