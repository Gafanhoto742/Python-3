'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário 
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a 
soma entre elas (desconsiderando o flag).'''


num = cont = soma = 0
while True:
    num = int(input('Digite um valor [Digite 999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números e a soma entre eles da {soma}!')