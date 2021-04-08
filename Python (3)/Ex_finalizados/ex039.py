'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do 
 tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''


from datetime import date
atual = date.today().year
print('-=-' * 20)
print('Pesquisa de alistamento Militar')
print('-=-' * 20)
nome = str(input('Digite o seu nome: ')).upper()
print('''Escolha um número para representar o seu sexo: 
[1] - HOMEM
[2] - MULHER''')
sexo = int(input('Digite a sua opção: '))
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print ('{} você nasceu em {} tem {} anos e está registrando essa informação no ano de {}'.format(nome, nasc, idade, atual))
if sexo == 1 and idade ==18:
    print('Você precisa fazer o alistamento obrigatório')
    print ('Você deve se alistar IMEDIATAMENTE!')
elif sexo == 1 and idade < 18:
    saldo = 18 - idade
    print('Falta {} ano(s) para você se alistar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será no ano de {}'.format(ano))
elif sexo == 1 and idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} ano(s) atrás'.format(saldo))
    ano =  atual - saldo
    print('Seu alistamento foi no ano de {}!'.format(ano))
else:
    print('{}, você não precisa realizar o alistamento militar obrigatório'.format(nome))
