# como adicionar itens em dicionario + lista em um looping + formatação

estado = {} # {} = dicionário
brasil = [] # [] lista
for c in range (0,3):
    estado['uf']= str(input('Unidade Federativa: '))
    estado['Sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # quando temos esse misto de dicionário e lista temos que inserir o copy para o dicionário, não podemos fatiar igual lista
for e in brasil:
    print(e)

estado = {} # {} = dicionário
brasil = [] # [] lista
for c in range (0,2):
    estado['uf']= str(input('Unidade Federativa: '))
    estado['Sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # quando temos esse misto de dicionário e lista temos que inserir o copy para o dicionário, não podemos fatiar igual lista
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')


estado = {} # {} = dicionário
brasil = [] # [] lista
for c in range (0,2):
    estado['uf']= str(input('Unidade Federativa: '))
    estado['Sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # quando temos esse misto de dicionário e lista temos que inserir o copy para o dicionário, não podemos fatiar igual lista
for e in brasil:
    for v in e.valeus():
        print(v, end=' ')
    print ( )