'''teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = '22'
galera.append(teste[:])
print(galera)

#como mostrar a estrutura composta completa
print('Demonstrando toda estrutura')
turma = [['Amanda',32], ['Gabriel',12], ['Henrique',35]]
print (turma)

#como mostrar a parte da estrutura, exemplo estou demonstrando a lista zero, 
# vai trazer todas infos que possui nesta lista
print ('Lista composta - Demonstrando uma lista completa')
turma = [['Amanda',32], ['Gabriel',12], ['Henrique',35]]
print (turma[0])

#como mostrar a parte da estrutura, exemplo estou demonstrando a lista zero, 
# e quero saber apenas a idade da pessoa da primeira lista
print('Lista composta - Demonstrar apenas 1 detalhe da lista Zero - Neste caso quero saber apenas a idade')
turma = [['Amanda', 32], ['Gabriel', 12], ['Henrique',35]]
print (turma[0][1]) # Lista 0 = Amanda, 32, vou trazer apenas a idade
print (turma[2][0]) # lista 2 = Henrique, 35, vou trazer apenas o nome

turma = [['Amanda', 32], ['Gabriel', 12], ['Henrique',35]]
for p in turma: #p = pessoas
    print (f'{p[0]} tem {p[1]} de idade!')


galera = []
dado = []
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print (galera)
'''


galera = []
dado = []
maior = menor = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    #dado.append(str(input('Apelido: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print (f'{p[0]} é menor de idade!')
        menor += 1
print(f'Temos {maior} maiores de idade e {menor} menores de idade')





