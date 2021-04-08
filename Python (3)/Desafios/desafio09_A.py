# Crie um programa q leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas
# O nome com todas letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Qual é o seu nome completo: '))
print ('O seu nome em maísculas ficarai deste formato {}'.format(nome.upper()))
print ('O seu nome em minusculsa ficaraia assim: {}' . format(nome.lower()))
print (nome.split())
dividido = nome.split ()
print ('O seu primeiro nome é {} e o seu primeiro nome tem {} letras'.format(dividido[0], len(dividido[0])))
print ('O o seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))