'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão.'''

print ('=' * 27)
print ('    10 TERMOS DE UMA PA')
print ('=' * 27)
t = float(input('Primeiro Termo: '))
r = float(input('Razão: '))
a = t
for c in range (1,11):
    a +=r
    print('{}'.format(a), end=' > ')
print ('FIM')


#Como demonstrado na video Aula
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razao
for c in range (primeiro, décimo, razao):
    print ('{}'.format(c),end=' ->')
print('FIM')

