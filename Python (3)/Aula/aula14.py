'''
for c in range (1,10):
    print(c)
print ('FIM')

Mesma for de escrita, mas o while pode ser utilizado para quando não sabemos o limite de repetições.
c = 1
while c < 10:
    print(c)
    c += 1
print ('FIM')
'''

'''
for c in range (1,5):
    n = int(input('Digite um valor: '))
print ('FIM")

mesma escrita mas com infinitas vezes de repetição até pertar 0
n = 1
while n != 0:
    n = int(input('Digite um número: '))
print ('FIM')
'''
'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja Continuar [S/N]: ')).upper()
print ('FIM')
'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0 :
        par += 1
    else:
        impar += 1
print ('Você digitou {} números pares e {} números impares!'.format(par,impar))
print ('FIM')