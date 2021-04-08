'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
print('-=-' *20)
velocidade = float(input('\033[1mQual é a velocidade atual do carro?\033[m '))
print('-=-' *20)
if velocidade > 80:
    print('\033[1;31mMULTADO!\033[m  Você excedeu o \033[33mlimite permitido que é 80 Km/h.\033[m')
    multa = (velocidade -80 ) * 7
    print ('Você deve pagar uma \033[1;31mmulta de R${:.2f}\033[m'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')