'''Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite. '''

veloc = float(input('Qual a velocidade do carro que estava o seu carro? '))
multa = input(veloc - 80)
vlmulta = input(multa * 7,00)
if veloc >=80.1:
    print('Você foi multado! E pagará R$ {:.2f}!'.format(vlmulta))
else:
    print('Parabéns, você está andando dentro do limite da via.')

