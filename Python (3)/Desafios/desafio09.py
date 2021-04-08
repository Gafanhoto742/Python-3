frase = 'Curso em Video Python'
print (frase[1:15:2])
print (frase.count('o'))
print(len(frase.strip())) #leitura len de espaços tamanho de frases e strip elimina espaços em braco
print(frase.replace('Python','Android')) #replace muda uma palavra pela outra mas esse formato substitui apenas essa linha de comando. para salvar esse processo tem que escrever como abaixo
frase = frase.replace('Python','Android') #assim será salvo a nova palavra para o comando
print(frase.find('Video'))# find é para encontrar uma palavra na linha string 9 do script
print(frase.split()) #split cria uma lista
dividido = frase.split ()
print (dividido[2]) #tras a palavra q está na string 2 (video), lembrando que sempre começa do 0,1,2
print (dividido[2][3]) # tras a palavra q está na string 2 e elemento (letra) 3 = e





#como colocar um texto 
print("""Leitura e gravação em arquivos com Python
Uma das tarefas mais importantes que realizamos no dia-a-dia é a manipulação de dados gravados em arquivos, dos mais variados tipos. Por exemplo, um administrador de sistemas precisa, com frequência, acessar informações de configuração armazenadas em arquivos de texto, e muitas vezes, efetuar alterações nesses arquivos.""")