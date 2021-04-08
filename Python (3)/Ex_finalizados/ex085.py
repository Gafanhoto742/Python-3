'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em 
uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores 
pares e ímpares em ordem crescente.'''

num = [[], []]
valor = 0
for c in range (1,8):
    
    print('-'*30)
    
    valor = int(input(f'Digite {c}º número: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

    

print('-'*30)
print(f'Você digitou os números: {num}')
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')