''' criar rotina exemplo escrever uma linha --- para separa assuntos, vc pode criar uma rotina e assim 
vc escreve uma vez e replica quantas vezes quiser com rotinas ex:'''

#sempre usar a palavra def....: e o sinal dois :

def mostralinha():
    print('-'*30)


mostralinha()
print(f'{"CONTINUE APRENDENDO PYTHON":^30}')
mostralinha()

mostralinha()
print(f'{"HENRIQUE UMA HORA VC APRENDE!":^30}')
mostralinha()

mostralinha()
print(f'{"AGORA VAI!":^30}')
mostralinha()

# como criar parametros de rotina, exemplo abaixo

def tit(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

tit(f'{"HENRIQUE OLIVEIRA":^30}')
tit(f'{"VC ESTÁ EM EVOLUÇÃO":^30}')
tit(f'{"TENHA PACIÊNCIA":^30}')

def soma(a,b):
    s = a + b
    print(f'{s}')

soma(4,5)
soma(8,9)
soma(2,1)

#outro exemplo de rotina com somas

def soma2(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} e {b} é = {s}')

soma2(b=4,a=5)
soma2(7, 2)

# Empacotar parametros de rotina - exemplo criamos uma tupla
def contador(* num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


# O empacotar permite fazer todos os parametros aplicaveis em tuplas ex:

def cont(*num1):
    for valor in num1:
        print('='*10)
        print (f'{valor:^10}')
        print('='*10)

cont(2, 1, 7)
cont(8, 0)
cont(4, 4, 7, 6, 2)

# O empacotar permite fazer todos os parametros aplicaveis em tuplas ex: com formatação

def cont1(*num1):
    for valor in num1:
        print (f'{valor:^10}', end=' ')
    print('FIM')


cont1(2, 1, 7)
cont1(8, 0)
cont1(4, 4, 7, 6, 2)


# contar elementos de num ( Len ) - tuplas não são mutaveis - desempacotar
def cont2(*num2):
    tam = len(num2)
    print (f'Recebi os valores {num2} e são ao todo {tam}', end=' ')
    print('- FIM')


cont2(2, 1, 7)
cont2(8, 0)
cont2(4, 4, 7, 6, 2)

#Model lista de desempacotar 

def soma1(* valores2):
    s = 0
    for nums in valores2:
        s += nums
    print(f'Somando os valores {valores2} temos {s}')

soma1(5 , 2)
soma1(2, 9, 4)




# como editar listas em rotina - lista é mutavel 
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2 #vai receber o dobro
        pos += 1 

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)