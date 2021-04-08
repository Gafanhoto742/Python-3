

# utilizar o help(), ajuda validar funções e parametros


# Primeiro exemplo de Documentação de função: neste caso vamos documentar com Docstrings
#para aplicar essa função, temos de digitar 3 aspas duplas no inicio e fim da documentação, sempre aplicar
# abaixo do def
'''
def contador (i,f,p):
    """
    ->Faz uma contagem e mostra na tela.
    :param i= inicio da contagem
    :param f= fim da contagem
    :param p= passo de contagem
    :return = sem retorno
    Função criada por Gustavo Guanabara
    """
    c = 1
    while c <= f:
        print(f'{c}',end =' ')
        c += p
    print('FIM')


#PROGRAMA PRINCIPAL
contador(2,10,2)

# como fazer consulta da documentação escrita referente ao programa acima 
help(contador)
'''
'''______________________________________________________________________________'''
'''
#####
#Parametros Opcionais

#modelo
def somar(a,b,c):
    s = a + b + c
    print(f'A soma vale {s}')

#programa principal
somar(3,2,5)
'''

'''______________________________________________________________________________'''
'''
#como incluir o parametro opcional, exemplo em C não indenfiquei o valor, para não dar erro devemos colocar c=0
#caso não tenho outro valor apontado o C será zerado, veja exemplo acima vs exemplo abaixo para compreender
# o programa principal está com valores de A e B.

# se colocar = 0 em todos param a=0, b=0, c=0, o programa executa mesmo se estiver zerado os valores no programa
#principal
def somar(a,b,c=0):
    """
    ->Faz uma soma de três valores e mostra resultado na tela.
    :param a= primeiro valor
    :param b= segundo valor
    :param c= terceiro valor
    :return = sem retorno
    Função criada por Gustavo Guanabara
    """
    s = a + b + c
    print(f'A soma vale {s}')

#programa principal
somar(8,4)
'''

'''_______________________________________________________'''
#ESCOPO DE VARIAIS

# neste formato o N1 global, permanece = 2, e o n1 dentro se torna uma variavel nova
'''
def função():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
print(f'N1 global vale {n1}')'''

'''
# neste formato usando a palavra GLOBAL, conseguimos informar que o  valor do N2 será substituido pelo valor
#apontado dentro. 

def funçãonova():
    global n2
    n2 = 8
    n3 += 4
    n4 = 2
    print(f'N1 dentro vale {n2}')
    print(f'N1 dentro vale {n3}')
    print(f'N1 dentro vale {n4}')

n2 = 5
funçãonova(n2)
print(f'n1 fora vale {n1}')'''


'''_____________________________________'''
#função com retorno

def somar(a=0, b=0, c=0):
    s = a + b + c 
    return s

r1= somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2}, {r3}')
