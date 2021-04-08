'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('aprender', 'programar', 'línguagem', 'python',
'curso', 'grátis', 'estudar', 'praticar',
'trabalhar', 'mercado', 'programador', 'futuro')

print ('-'*40)
print(f'\033[7;30;39m{"DEMONSTRAÇÃO DAS VOGAIS DE UMA PALAVRA":^40}\033[m')
print('-'*40)

for p in palavras:
    print (f'\nNa palavra \033[33m{p.upper()}\33[m temos ', end='')
    for letra in p:
        if letra.lower() in 'aáàâãeéiíoóôõuú':
            print (f'\033[33m{letra.upper()}\33[m', end=' ')