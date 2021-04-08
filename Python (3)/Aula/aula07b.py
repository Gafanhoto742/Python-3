nome = input('Qual é o seu nome?')
print('É um prazer te conhecer {}'.format(nome))
print('{}, vamos testar o seu conhecimento em operadores aritméticos'.format(nome))
n1=int(input('Digite um número:'))
n2=int(input('Digite outro número: '))
n3=int(input('Digite mais um número:'))
resp=(n1+n2)*n3
print('Você sabia que {} + {} * {} é igual = {}'.format(n1, n2, n3, resp))
