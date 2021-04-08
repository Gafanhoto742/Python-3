#Dobro,Triplo, Raiz Quadrada
n = int(input('Digite um número: '))
d = n*2 #dobro
t = n*3 #triplo
r =  n ** (1/2)

print('Você sabia que o dobro de {} é {} '.format(n,d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n,t,n,r))

# outro metodo para o mesmo exercicio
#n = int(input('Digite um número: '))
#print('O dobro de {} vale {}.'.format(n,(n*2)))
#print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(n,(n*3),n,(n**(1/2))))
