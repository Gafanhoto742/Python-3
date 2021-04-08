def fatorial(num=1):
    f = 1
    for c in range (num, 0 , -1):
        f *=c
    return f

#pode ser assim
'''
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual à {fatorial(n)}')'''

#pode ser assim
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')



'''-------------------'''
#return de verdadeiro ou falso

def par (n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
'''print(par(num))'''
if par(num):
    print('É par!')
else:
    print('Não é par!')