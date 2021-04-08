'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
km = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de \033[1;32m{:.2f}Km\033[m.'.format(km))

# script, sem orientação
'''
vl1 = km * 0.50
vl2 = km * 0.45
if km <200 :
    print('E o preço da sua passagem será de \033[1;31mR${:.2f}\033[m'.format(vl1))
else:
    print('E o preço da sua passagem será de \033[1;31mR${:.2f}\033[m'.format(vl2)) '''

#Apresentação do Professor
'''
if km <=200:
    vl = km * 0.50
else:
    vl = km * 0.45
print('E o preço da sua passagem será de \033[1;31mR${:.2f}\033[m'.format(vl)) '''

#como escrever o mesmo script de forma reduzida
vl = km * 0.50 if km <=200 else km *0.45
print('E o preço da sua passagem será de \033[1;31mR${:.2f}\033[m'.format(vl))