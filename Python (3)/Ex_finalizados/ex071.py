'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual 
será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$5. '''

print('='*40)
print('{: ^40}'.format('CAIXA ELETRÔNICO'))
print('='*40)
saque = int(input('Qual valor você gostaria de sacar? R$'))
tot = saque
cedula = 50
totced = 0
while True:
    if tot >= cedula:
        tot -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        totced = 0
        if tot == 0:
            break
print('Obrigado volte sempre!')

