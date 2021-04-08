for c in range (0, 6): # ele sempre ignora o ultimo numero da referencia
    print('Teste')
print ('FIM')

for c in range (1, 6): # ele sempre ignora o ultimo numero da referencia (contagem progressiva)
    print(c)
print ('FIM')

for c in range (6 , 0, -1): #contagem regressiva
    print(c)
print ('FIM')

for c in range(0, 7, 2): #contagem de dois em dois
    print(c)
print('FIM')

n = int(input('Digite um número: ')) #comando para contar até o numero digitado
for c in range (0, n+1):
    print(c)
print ('FIM')

n= int(input('Digite um número: '))
for c in range (0, n+1, 2):
    print (c)
print('FIM')

i = int(input('Início: ')) 
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('FIM')

for c in range (0, 3 ): # leu uma vez, mas repetiu 3 vezes porque está no for
    n = int(input('Digite um valor: '))
print ('FIM')

s = 0 # como realizar somatório em repetições
for c in range (0, 4 ):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
