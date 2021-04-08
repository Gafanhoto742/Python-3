'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres 
têm menos de 20 anos.'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ' '
totm = 0
totf = 0
for n in range (1,5):
    print ('----{}ª PESSOA----'.format(n))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if n == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'M':
        totm += 1
        
    if sexo == 'F':
        totf += 1
        
mediaidade = somaidade / 4
print ('A média de idade do grupo é de {:.2f} anos'.format(mediaidade))
print ('O Homem mais velho tem {} e se chama {}.')
print ('Ao todo são {} mulheres com menos de {} anos.')
