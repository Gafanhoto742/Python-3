'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos 
e fechados na ordem correta.'''
'''
lista1 = []
lista2 = []
e = input('expressão: ')
for c in e:
    if c == '(':
        lista1.append(c)
    elif c == ')':
        lista2.append(c)
if len(lista1) == len(lista2):
    print('Expressão correta')
else:
    print('Expressão errada')
'''


expr = str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão Correta')
else:
    print('Expressão Errada')    
    