'''Python – Fase 09 – Manipulando Strings
Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender 
são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), 
title(), strip(), junção com join().'''

nome = str (input ('Digite o seu nome: ')).strip()
print ('Analisando seu nome ....')
print ('Seu nome em maiúsculas é {}'.format(nome.upper()))
print ('Seu nome em minusculas é {}'.format(nome.lower()))
print ('Seu nome tem ao todo {} letas.'.format(len(nome)-nome.count(' ')))
#print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))