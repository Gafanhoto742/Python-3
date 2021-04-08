nome = str(input('Qual é o seu nome? '))
if nome == 'Henrique':
    print('Que nome bonito!')
elif nome == 'Amanda' or nome == 'Gabriel' or nome == 'Ben': # ou
    print ('Você tem o nome de um dos meus anjos')
elif nome in 'Ana Claúdia Jéssoca Juliana': #igual
    print ('Belo nome feminino')
else:
    print ('Seu nome é bem normal!')
print ('Tenha um bom dia, {}'.format(nome))