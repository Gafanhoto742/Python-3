#dicionários

# mostrando o dicionário inteiro
pessoas = {'Nome': 'Henrique','Sexo':'M', 'Idade':'35'}
print(pessoas) 


# mostrar 1 intem do dicionário
pessoas = {'Nome': 'Henrique', 'Sexo':'M', 'Idade': '35'}
print(pessoas['Idade'])
print(pessoas.keys()) # como mostrar tudo que tem dentro da chave 
print(pessoas.values()) # mostra os valores
print(pessoas.items()) # mostra os itens


# ao mostrar itens formatados não esquecer de usar ""
endereco = {'Rua': 'Rua Sei lá', 'CEP': '01010-000','UF': 'SP'}
print(f'Você está situado em {endereco["Rua"]} com o no estado {endereco["UF"]}')


# utilizando laços para Keys
tarefas = {'Lavar Louça':'Amanda','Aspirar a casa': 'Henrique', 'Passar pano': 'Gabriel'}
for k in tarefas.keys(): #k = keys
    print(k)

# utilizando itens = substituir o enumared
tarefas = {'Lavar Louça':'Amanda','Aspirar a casa': 'Henrique', 'Passar pano': 'Gabriel'}
for k, v in tarefas.items(): 
    print(f'{k} = {v}')

# Como excluir um elemento
pessoas = {'Nome': 'Henrique','Sexo':'M', 'Idade':'35'}
del pessoas['Sexo']
for k, v  in pessoas.items():
    print(f'{k} = {v}') 

# Como Adicionar outro nome elemento e também como adicionar nova Key
pessoas = {'Nome': 'Amanda', 'Sexo': 'F', 'Idade': '32'}
pessoas ['Nome'] = 'Mands'
pessoas ['Time'] = 'Parmeira'
for k, v in pessoas.items():
    print(f'{k} = {v}')

#Como adicionar um Dicionário dentro de uma lista

brasil = [] #lista

#dicionário
estado1 = {'uf': 'São Paulo', 'Sigla': 'SP'}
estado2 = {'uf': 'Bahia', 'Sigla': 'BA'}

brasil.append(estado1)
brasil.append(estado2)

print(estado1) # vai mostrar os itens como lista
print(brasil) # vai mostrar uma lista e dentro da lista vai mostrar os elementos dicionario
print(brasil[0]) # vai mostrar o primeiro estado adicionado
print(brasil[0]['uf']) # vai mostrar o primeiro UF adiconado SP

# como adicionar itens em dicionario + lista em um looping

estado = {} # {} = dicionário
brasil = [] # [] lista
for c in range (0,3):
    estado['uf']= str(input('Unidade Federativa: '))
    estado['Sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # quando temos esse misto de dicionário e lista temos que inserir o copy para o dicionário, não podemos fatiar igual lista
print(brasil)