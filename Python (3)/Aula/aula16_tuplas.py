
# for sem mostrar posição
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print ('Comi pra caramba!')

#For demonstrando a posição
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print ('Comi pra caramba!')

lanche = ('Hambúrguer', 'Suco', ' Pizza', ' Pudim', 'Batata Frita')
for pos, comida in enumerate(lanche):
    print (f'Eu vou comer {comida} na posição {pos}')
print ('Comi pra caramba!')

#Demonstrar em ordem (Alfabetica)
lanche = ('Hambúrguer', ' Suco', 'Pizza', 'Batata Frita')
print (sorted(lanche))
print(lanche)

#Tupla que junta A e B
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print (c)

# Len de c (quantos elementos)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print (len(c))

'''# Cont de c (quantas vezes aparece o numero 5)
a = (2, 5, 4)
b = (5, 8, 1, 2)
z = b + a
print (z.cont(5))'''

# Index de c (em que posição aparece o numero 8)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print (c)
print (c.index(8))

#
pessoa = ('Henrique', 35, 'M', 70.20)
print (pessoa)