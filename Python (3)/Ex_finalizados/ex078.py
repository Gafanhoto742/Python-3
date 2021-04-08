
'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''

''' como eu escrevi'''
maior = menor = 0

val = []

for cont in range (0,5): #5 ler valores para uma lista
    val.append(int(input(f'\nDigite o um valor para posição {cont}:')))

    if cont  == 0 :
        maior = menor = val[cont]

    else:
        if val[cont] > maior:
            maior = val[cont]
        if val[cont] < menor:
            menor = val[cont]
        

print('-'*30)

print()

print(f'Você digitou os valores: {val}')

print()




for c, v in enumerate(val): #mostra valores que digitou e posição que estão
    print(f'\nNa posição {c} encontrei o valor {v}')
    
print(f'\nO maior valor digitado foi {maior} na(s) posição: ',end='')
for c, v in enumerate(val):
    if v == maior:
        print(f'{c}...',end='')
print('\n')



print(f'\nO MENOR valor digitado foi {menor} na(s) posição: ',end='')
for c, v in enumerate(val):
    if v == menor:
        print(f'{c}...',end='')
print('\n')


print('-'*30)
print('\n\nCheguei ao final da lista digitada por você')




''' formato do professor Guanabara
maior = menor = 0

val = []
for cont in range (0,5): #5 ler valores para uma lista
    val.append(int(input(f'\nDigite o um valor para posição {cont}:')))

    if cont  == 0 :
        maior = menor = val[cont]

    else:
        if val[cont] > maior:
            maior = val[cont]
        if val[cont] < menor:
            menor = val[cont]
        


print('-'*30)
print(f'\nVocê digitou os valores {val}')
print(f'\nO maior valor digitado foi {maior} na(s) posição: ',end='')
for c, v in enumerate(val):
    if v == maior:
        print(f'{v}...',end='')
print('\n')

print(f'\nO MENOR valor digitado foi {menor} na(s) posição: ',end='')
for c, v in enumerate(val):
    if v == menor:
        print(f'{v}...',end='')
print('\n')
    

print('-'*30)


print('\n\nCheguei ao final da lista digitada por você')
'''