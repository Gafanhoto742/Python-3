''' Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, 
ANOTARAM A DATA DA MARATONA.'''

frase = str(input('Digite uma frase: ')).strip().upper() #strip para tirar espaços antes e depois e Upper para ficar tudo em maiuscula
palavras = frase.split() #criou uma lista
junto = ''.join(palavras) #join subtitue os espaços, neste caso estou removendo espaço, mas posso colocar sinais para substituir * , _ - +
inverso = ''
for letra  in range (len(junto)-1, -1, -1): #busca da ultima letra (len)
    inverso += junto[letra]
print ('O inverso de {} é {}'.format(junto, inverso))
if inverso  == junto: #teste se o inverso é igual a frase digitada
    print('Essa frase é um \033[34mPALÍNDROMO\033[m')
else:
    print('Essa frase é um \033[34mNÃO É UM PALÍNDROMO\033[m')

#outra maneira de escrever o mesmo codigo
frase = str(input('Digite uma frase: ')).strip().upper() #strip para tirar espaços antes e depois e Upper para ficar tudo em maiuscula
palavras = frase.split() #criou uma lista
junto = ''.join(palavras) #join subtitue os espaços, neste caso estou removendo espaço, mas posso colocar sinais para substituir * , _ - +
inverso = junto[::-1] #fatiamento
print ('O inverso de {} é {}'.format(junto, inverso))
if inverso  == junto: #teste se o inverso é igual a frase digitada
    print('Essa frase é um \033[34mPALÍNDROMO\033[m')
else:
    print('Essa frase é um \033[34mNÃO É UM PALÍNDROMO\033[m')