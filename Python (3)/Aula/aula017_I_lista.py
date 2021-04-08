num = [2, 5, 9, 1]
num[2]=10 # substituir o valor que está no espaço 2 , exemplo 9, para 10
num.append(7) # adicionar um numéro ou testo na lista, sempre usando .append()
num.sort() # colocar a lista em ordem alfabetica ou númerica
print (num)
print(f'Essa lista tem {len(num)} elementos') #demonstrar quantos elementos tem em uma lista


num = [2, 5, 9, 1]
num[2]=10 # substituir o valor que está no espaço 2 , exemplo 9, para 10
num.append(7) # adicionar um numéro ou testo na lista, sempre usando .append()
num.sort(reverse=True) # coloco a lista de trás pra frente do ultima ao primeiro
print (num)
print(f'Essa lista tem {len(num)} elementos') #demonstrar quantos elementos tem em uma lista

num = [8, 9, 10, 12]
num[2] = 100 # substituir o valor que está no espaço 2 , exemplo 9, para 100
num.append(300) # adicionar um numéro ou testo na lista, sempre usando .append()
num.sort() #colocar a lista em ordem alfabetica ou númerica
num.insert (2, 0) # Adicionar mais numeros na lista, neste caso inseri o número zero na casa 2 e deslocando os números
print (num)
print(f'Essa lista tem {len(num)} elementos') #demonstrar quantos elementos tem em uma lista

num = [8, 9, 10, 12]
num[2] = 100 # substituir o valor que está no espaço 2 , exemplo 9, para 100
num.append(300) # adicionar um numéro ou testo na lista, sempre usando .append()
num.sort() #colocar a lista em ordem alfabetica ou númerica
num.insert (2, 0) # Adicionar mais numeros na lista, neste caso inseri o número zero na casa 2 e deslocando os números
num.pop() # se deixarmos () sem valor, vamos eliminar o ultimo numero  - Se colocar (2) vamos eliminar o intem elemento 2
print (num)
print(f'Essa lista tem {len(num)} elementos') #demonstrar quantos elementos tem em uma lista

num = [8, 9, 10, 12]
num[2] = 100 # substituir o valor que está no espaço 2 , exemplo 9, para 100
num.append(300) # adicionar um numéro ou testo na lista, sempre usando .append()
num.sort() #colocar a lista em ordem alfabetica ou númerica
num.insert (2, 0) # Adicionar mais numeros na lista, neste caso inseri o número zero na casa 2 e deslocando os números
num.pop() # se deixarmos () sem valor, vamos eliminar o ultimo numero  - Se colocar (2) vamos eliminar o intem elemento 2
print (num)
print(f'Essa lista tem {len(num)} elementos') #demonstrar quantos elementos tem em uma lista

num = [8, 9, 10, 12]
num[2] = 100 # substituir o valor que está no espaço 2 , exemplo 9, para 100
num.append(300) # adicionar um numéro ou testo na lista, sempre usando .append()
num.sort() #colocar a lista em ordem alfabetica ou númerica
num.insert (2, 2) # Adicionar mais numeros na lista, neste caso inseri o número zero na casa 2 e deslocando os números
num.remove(2) # se deixarmos (2) valor já existente de uma lista e duplicado será removido apenas o primeiro elemento do mesmo valor
print (num)
print(f'Essa lista tem {len(num)} elementos') #demonstrar quantos elementos tem em uma lista

num = [2, 5, 9, 10]
num[2] = 100 # substituir o valor que está no espaço 2 , exemplo 9, para 100
num.append(300) # adicionar um numéro ou testo na lista, sempre usando .append()
num.sort() #colocar a lista em ordem alfabetica ou númerica
num.insert (2, 2) # Adicionar mais numeros na lista, neste caso inseri o número zero na casa 2 e deslocando os números
if 4 in num: #uso do in é muito importante para condições de lista
    num.remove(4) # Neste caso não temos o número 4 na lista, caso não tiver o IF, o código vai dar erro.
else:
    print('Não achei o número 4')
print (num)
print(f'Essa lista tem {len(num)} elementos') #demonstrar quantos elementos tem em uma lista

num = [2, 5, 9, 10]
num[2] = 100 # substituir o valor que está no espaço 2 , exemplo 9, para 100
num.append(300) # adicionar um numéro ou testo na lista, sempre usando .append()
num.sort() #colocar a lista em ordem alfabetica ou númerica
num.insert (2, 2) # Adicionar mais numeros na lista, neste caso inseri o número zero na casa 2 e deslocando os números
if 5 in num: #uso do in é muito importante para condições de lista
    num.remove(5) # Neste caso temos o número 5 na lista, o código com IF vai validar e realizar a exclusão do número
else:
    print('Não achei o número 5')
print (num)
print(f'Essa lista tem {len(num)} elementos') #demonstrar quantos elementos tem em uma lista

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores: # para cada valor em valores, print
    print(f'{v}...',end='') # end='' é para deixar todos os resultados em uma única linha


valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores): # enumerate() trazer a chave dentro dos valores
    print(f'\nna posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


valores = []
for cont in range (0,5): #ler valores e colocar dentro de uma lista
    valores.append(int(input('Digite um valor: '))) # informar os valores a ser registrado

for c, v in enumerate(valores): #mostra valores que digitou e posição que estão
    print(f'\nNa posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista digitada por você')


a = [2, 3, 4, 7]
b = a #LIGAÇÃO da lista A para B
b[2]= 8 #CUIDADO como uma lista é uma ligação, ele altera os valores das duas listas A e B

print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]
b = a[:] # [:] COPIA da lista A para B
b[2]= 8 #Quando for uma cópia de uma lista, podemos ver que ele altera os valores somente listas B

print(f'Lista A: {a}')
print(f'Lista B: {b}')

